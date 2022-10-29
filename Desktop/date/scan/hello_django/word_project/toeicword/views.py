from pyexpat.errors import messages
#from typing import ParamSpec
from django.shortcuts import render
from django.http import HttpResponse

from .models import MyWord #追加部

from django.contrib import messages#単語登録に成功した時ウや失敗した時に表示する文字列を設定するための物
from .forms import RegistrationForm#単語登録ページのviewに必要なため


# Create your views here.
def index(request):
    return render(request, 'toeicword/index.html')
#renderは、第二引数で指定したhtmlファイルをブラウザに表示してくれる
#第三引数を指定して、htmlファイルへ第三引数に入っている変数を使うこともできる。
# トップページの作成では不必要

#追加:単語リストページための関数
def wordlist(request):
    wordlist = MyWord.objects.all()#MyWordに入っている英単語と日本語訳の一覧が代入される
    
    params = {
        'words':wordlist
    }#paramsは辞書形、htmlファイルで使う変数名と変数が代入される
    
    return render(request, 'toeicword/wordlist.html', params)
    #renderでは、第三引数を指定することで、第三引数に入っている変数をhtmlファイルで使うことができる
    
#単語登録ページのviewである。
def wordregistration(request):
    if (request.method == 'POST'):#単語を登録するボタンを押されたことを判定している。
        regi_en_word = request.POST['en_word']
        regi_jp_word = request.POST['jp_word']
        #上二行：送信されてきた英単語と日本語訳を変数に代入している
        exist = MyWord.objects.filter(en_word=regi_en_word)
        #上：モデルから同じ英単語が登録されているか、検索をかける
        
        #下if文：existの大きさが0であれば同じ英単語が登録されていないことになる
        #逆に0以上であれば同じ単語がすでに登録されていることになる
        #if文の中では、モデルに単語を代入して保存している
        if (len(exist) == 0):
            mw = MyWord()
            mw.en_word = regi_en_word
            mw.jp_word = regi_jp_word
            mw.save()
            messages.success(request, '登録しました！')#messagesに第二引数の文字列が表示される
        else:#単語の保存に失敗下時に表示される
            messages.error(request, '登録できませんでした。既に登録されています。')
            
    form = RegistrationForm()
    
    params = {
        'form': form,
    }
    
    return render(request, 'toeicword/registration.html', params)

def worddelete(request):
    #下2行：変数の初期化する
    del_en_word = ''
    del_jp_word = ''
    if ('del_id' in request.GET):#削除する単語が指定されているか確認
        del_id = request.GET['del_id']#URLからdel_idパラメータのデータを取り出し、変数に代入
        mws_obj = MyWord.objects.filter(id=del_id).first()
        #上：del_idに代入されているidから、MyWordに格納されている単語を取り出している
        del_en_word = mws_obj.en_word
        del_jp_word = mws_obj.jp_word
        #67~68：65行目で鳥出した単語をそれぞれ変数に代入
#ここまでが、単語リストページから削除ボタンをクリックして、単語削除ページに単語を表示する処理
    if (request.method == 'POST'):#単語削除ページから送られてきたデータであることを確認
        word_delete = request.POST['en_word']#削除する単語を変数に代入
        MyWord.objects.filter(en_word=word_delete).delete()#実際にMyWordモデルからデータ（単語）を削除
        messages.success(request, '{0}を削除しました。'.format(word_delete))
        #上：messagesを使ってデータが削除されたことを伝えるメッセージを表示する設定を行っている
#以上までが、単語削除ページから削除ボタンをクリックして、実際にデータ（単語）を削除するまでの処理
    params = {
    'del_en_word': del_en_word,
    'del_jp_word': del_jp_word,
    }

    return render(request, 'toeicword/worddelete.html', params)

def wordedit(request):#関数の宣言
    #変数初期化
    ed_en_word = ''
    ed_jp_word = ''
    #編集する単語が指定されているか確認している
    if ('ed_id' in request.GET):
        #下：URLからed_idパラメータのデータを取り出し、変数に代入
        ed_id = request.GET['ed_id']
        #下：ed_idに代入されているidから、MyWordaに格納されている単語を取り出している。
        mws_obj = MyWord.objects.filter(id=ed_id).first()
        #下二行：上の行で取り出した単語をそれぞれ変数に代入している
        ed_en_word = mws_obj.en_word
        ed_jp_word = mws_obj.jp_word
#ここまでは単語リストページから編集ボタンをクリックして、単語編集ページに単語が表示される処理である。
        
    if (request.method == 'POST'):#単語編集ページから送られてきたデータであることを確認する
        #下二行：送られてきた単語を変数に代入している
        en_word = request.POST['en_word']
        new_jp_word = request.POST['jp_word']
        #下一行：送られてきた英単語に一致する一行を取り出している。
        mws_obj = MyWord.objects.filter(en_word=en_word).first()
        #下一行：送られてきた一行の日本語の部分だけ上書きしている
        mws_obj.jp_word = new_jp_word
        mws_obj.save()#データ保存
        #下一行：messagesを使ってデータが編集されたことを伝えるメッセージを表示する設定を行う
        messages.success(request, '{0}を編集しました。'.format(en_word))
#以上までは、単語編集ページから編集ボタンをクリックして、実際にデータ（単語）を編集するまでの処理である。
    params = {
        'ed_en_word': ed_en_word,
        'ed_jp_word': ed_jp_word,
    }

    return render(request, 'toeicword/wordedit.html', params)

#問題選択や、正解・不正解の判定を行う機能を作成する
import numpy.random as random #モデル方単語を一つ選択するために使う
def answer(request):
    answer_message = ''#変数の初期化
    #下一行：解答ボタンをクリックしたかを判定する、
    # つまり、表示された英語に対して解答フォームに入力を行ったかを判定する
    if (request.method == "POST"):
        #下二行：送信されて来た英単語と回答を変数に代入
        problem_word = request.POST.get('en_problem')
        answer_word = request.POST.get('jp_answer')
        #下一行：mw_objに送信されてきた英語が格納されている一行を代入している
        mw_obj = MyWord.objects.filter(en_word=problem_word).first()
        #下一行：mw_objに格納されている日本語の部分を取り出している
        #日本語の部分は単語ト単語の間が全角のスペースで区切られているはずであるため、
        #split...によって文字列を分割する
        jp_list = mw_obj.jp_word.split('\u3000')
    #134~138:分割下文字列に送信されてきた日本語が含まれているかを判定する
        if (answer_word in jp_list):
            answer_message = "正解です。"
        else:
            answer_message = "不正解です。{0}の日本語訳は{1}".format(problem_word, jp_list)
    #下に行：モデルの中から英単語を一つだけを取り出している
    count_mw = MyWord.objects.count()# randint:任意の範囲の整数
    en_word = MyWord.objects.all()[random.randint(0, count_mw-1)]
    
    params = {
        'en_word': en_word,
        'answer_message': answer_message,
    }
    
    return render(request, 'toeicword/answer.html', params)