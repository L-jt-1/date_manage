from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World!')

from venv import create
from django.shortcuts import render
from django.http import HttpResponse

from .models import N_word #追加部
from .models import V_word
from .models import Adj_word
from .models import Adv_word
from .models import In_word
from .models import Other_word
from .models import Memo_word

import mytoeic.all_words as t_all_w
import mytoeic.my_weblio as t_my_weblio

from django.contrib import messages
from .forms import RegistrationForm

#引入模型
# Create your views here.
    
def index(request):
    return render(request, "mytoeic/index.html")

def n_wordlist(request):
    n_wordlist = N_word.objects.all()
    
    params = {
        'words':n_wordlist
    }
    
    return render(request, 'mytoeic/n_wordlist.html', params)

def v_wordlist(request):
    v_wordlist = V_word.objects.all()
    
    params = {
        'words':v_wordlist
    }
    
    return render(request, 'mytoeic/v_wordlist.html', params)

def adj_wordlist(request):
    adj_wordlist = Adj_word.objects.all()
    
    params = {
        'words':adj_wordlist
    }
    
    return render(request, 'mytoeic/adj_wordlist.html', params)

def adv_wordlist(request):
    adv_wordlist = Adv_word.objects.all()
    
    params = {
        'words':adv_wordlist
    }
    
    return render(request, 'mytoeic/adv_wordlist.html', params)

def in_wordlist(request):
    in_wordlist = In_word.objects.all()
    
    params = {
        'words':in_wordlist
    }
    
    return render(request, 'mytoeic/in_wordlist.html', params)

def other_wordlist(request):
    other_wordlist = Other_word.objects.all()
    #print(other_wordlist)
    params = {
        'words':other_wordlist
    }
    #print(params)
    return render(request, 'mytoeic/other_wordlist.html', params)

def memo_wordlist(request):
    memo_wordlist = Memo_word.objects.all()
    #print(other_wordlist)
    params = {
        'words':memo_wordlist
    }
    #print(params)
    return render(request, 'mytoeic/memo_wordlist.html', params)

def wordregistration(request):
    if(request.method == 'POST'):
        regi_en_word = request.POST['en_word']
        regi_jp_word = request.POST['jp_word']
        regi_word_type = request.POST['word_type']
        exist = Memo_word.objects.filter(en_word=regi_en_word)
        if(len(exist) == 0):
            mw = Memo_word()
            mw.en_word = regi_en_word
            mw.jp_word = regi_jp_word
            mw.word_type = regi_word_type
            mw.save()
            messages.success(request, '登録しました。')
        else:
            messages.error(request, "登録できませんでした。既に登録されています。")

    form = RegistrationForm()

    params = {
        'form':form,
    }

    return render(request, 'mytoeic/registration.html', params)

def n_worddelete(request):
    del_en_word = ''
    del_jp_word = ''
    del_word_type = ''
    #名詞削除
    if('del_id' in request.GET):
        del_id = request.GET['del_id']
        mws_obj = N_word.objects.filter(id=del_id).first()
            
        del_en_word = mws_obj.en_word
        del_jp_word = mws_obj.jp_word
        del_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        word_delete = request.POST['en_word']
        N_word.objects.filter(en_word=word_delete).delete()
        messages.success(request, '{0}を削除しました。'.format(word_delete))
    
    params = {
        'del_en_word':del_en_word,
        'del_jp_word':del_jp_word,
        'del_word_type':del_word_type,
    }
    return render(request, 'mytoeic/n_worddelete.html', params)

def v_worddelete(request):
    del_en_word = ''
    del_jp_word = ''
    del_word_type = ''
    #形容詞削除
    if('del_id' in request.GET):
        del_id = request.GET['del_id']
        mws_obj = V_word.objects.filter(id=del_id).first()
        
        del_en_word = mws_obj.en_word
        del_jp_word = mws_obj.jp_word
        del_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        word_delete = request.POST['en_word']
        V_word.objects.filter(en_word=word_delete).delete()
        messages.success(request, '{0}を削除しました。'.format(word_delete))
        
    params = {
        'del_en_word':del_en_word,
        'del_jp_word':del_jp_word,
        'del_word_type':del_word_type,
    }
    return render(request, 'mytoeic/V_worddelete.html', params)


def adj_worddelete(request):
    del_en_word = ''
    del_jp_word = ''
    del_word_type = ''
    #形容詞削除
    if('del_id' in request.GET):
        del_id = request.GET['del_id']
        mws_obj = Adj_word.objects.filter(id=del_id).first()
        
        del_en_word = mws_obj.en_word
        del_jp_word = mws_obj.jp_word
        del_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        word_delete = request.POST['en_word']
        Adj_word.objects.filter(en_word=word_delete).delete()
        messages.success(request, '{0}を削除しました。'.format(word_delete))
        
    params = {
        'del_en_word':del_en_word,
        'del_jp_word':del_jp_word,
        'del_word_type':del_word_type,
    }
    return render(request, 'mytoeic/adj_worddelete.html', params)

def adv_worddelete(request):
    del_en_word = ''
    del_jp_word = ''
    del_word_type = ''
    #副詞削除
    if('del_id' in request.GET):
        del_id = request.GET['del_id']
        mws_obj = Adv_word.objects.filter(id=del_id).first()
        
        del_en_word = mws_obj.en_word
        del_jp_word = mws_obj.jp_word
        del_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        word_delete = request.POST['en_word']
        Adv_word.objects.filter(en_word=word_delete).delete()
        messages.success(request, '{0}を削除しました。'.format(word_delete))
        
    params = {
        'del_en_word':del_en_word,
        'del_jp_word':del_jp_word,
        'del_word_type':del_word_type,
    }
    return render(request, 'mytoeic/adv_worddelete.html', params)

def in_worddelete(request):
    del_en_word = ''
    del_jp_word = ''
    del_word_type = ''
    #IN詞削除
    if('del_id' in request.GET):
        del_id = request.GET['del_id']
        mws_obj = In_word.objects.filter(id=del_id).first()
        
        del_en_word = mws_obj.en_word
        del_jp_word = mws_obj.jp_word
        del_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        word_delete = request.POST['en_word']
        In_word.objects.filter(en_word=word_delete).delete()
        messages.success(request, '{0}を削除しました。'.format(word_delete))
        
    params = {
        'del_en_word':del_en_word,
        'del_jp_word':del_jp_word,
        'del_word_type':del_word_type,
    }
    return render(request, 'mytoeic/in_worddelete.html', params)

def other_worddelete(request):
    del_en_word = ''
    del_jp_word = ''
    del_word_type = ''
    #他の品詞削除
    if('del_id' in request.GET):
        del_id = request.GET['del_id']
        mws_obj = Other_word.objects.filter(id=del_id).first()
        
        del_en_word = mws_obj.en_word
        del_jp_word = mws_obj.jp_word
        del_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        word_delete = request.POST['en_word']
        Other_word.objects.filter(en_word=word_delete).delete()
        messages.success(request, '{0}を削除しました。'.format(word_delete))
        
    params = {
        'del_en_word':del_en_word,
        'del_jp_word':del_jp_word,
        'del_word_type':del_word_type,
    }
    return render(request, 'mytoeic/other_worddelete.html', params)

def memo_worddelete(request):
    del_en_word = ''
    del_jp_word = ''
    del_word_type = ''
    #メモ詞削除
    if('del_id' in request.GET):
        del_id = request.GET['del_id']
        mws_obj = Memo_word.objects.filter(id=del_id).first()
        
        del_en_word = mws_obj.en_word
        del_jp_word = mws_obj.jp_word
        del_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        word_delete = request.POST['en_word']
        Memo_word.objects.filter(en_word=word_delete).delete()
        messages.success(request, '{0}を削除しました。'.format(word_delete))
        
    params = {
        'del_en_word':del_en_word,
        'del_jp_word':del_jp_word,
        'del_word_type':del_word_type,
    }
    return render(request, 'mytoeic/memo_worddelete.html', params)
#単語編集ページ
def n_wordedit(request):
    ed_en_word = ''
    ed_jp_word = ''
    ed_word_type = ''
    if('ed_id' in request.GET):
        ed_id = request.GET['ed_id']
        mws_obj = N_word.objects.filter(id=ed_id).first()
        ed_en_word = mws_obj.en_word
        ed_jp_word = mws_obj.jp_word
        ed_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        en_word = request.POST['en_word']
        new_jp_word = request.POST['jp_word']
        mws_obj = N_word.objects.filter(en_word=en_word).first()
        mws_obj.jp_word = new_jp_word
        mws_obj.save()
        messages.success(request, '{0}を編集しました。'.format(en_word))

    params = {
        'ed_en_word':ed_en_word,
        'ed_jp_word':ed_jp_word,
        'ed_word_type':ed_word_type,
    }
    return render(request, 'mytoeic/n_wordedit.html', params)

def v_wordedit(request):
    ed_en_word = ''
    ed_jp_word = ''
    ed_word_type = ''
    if('ed_id' in request.GET):
        ed_id = request.GET['ed_id']
        mws_obj = V_word.objects.filter(id=ed_id).first()
        ed_en_word = mws_obj.en_word
        ed_jp_word = mws_obj.jp_word
        ed_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        en_word = request.POST['en_word']
        new_jp_word = request.POST['jp_word']
        mws_obj = V_word.objects.filter(en_word=en_word).first()
        mws_obj.jp_word = new_jp_word
        mws_obj.save()
        messages.success(request, '{0}を編集しました。'.format(en_word))

    params = {
        'ed_en_word':ed_en_word,
        'ed_jp_word':ed_jp_word,
        'ed_word_type':ed_word_type,
    }
    return render(request, 'mytoeic/v_wordedit.html', params)

def adj_wordedit(request):
    ed_en_word = ''
    ed_jp_word = ''
    ed_word_type = ''
    if('ed_id' in request.GET):
        ed_id = request.GET['ed_id']
        mws_obj = Adj_word.objects.filter(id=ed_id).first()
        ed_en_word = mws_obj.en_word
        ed_jp_word = mws_obj.jp_word
        ed_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        en_word = request.POST['en_word']
        new_jp_word = request.POST['jp_word']
        mws_obj = Adj_word.objects.filter(en_word=en_word).first()
        mws_obj.jp_word = new_jp_word
        mws_obj.save()
        messages.success(request, '{0}を編集しました。'.format(en_word))

    params = {
        'ed_en_word':ed_en_word,
        'ed_jp_word':ed_jp_word,
        'ed_word_type':ed_word_type
    }
    return render(request, 'mytoeic/adj_wordedit.html', params)

def adv_wordedit(request):
    ed_en_word = ''
    ed_jp_word = ''
    ed_word_type = ''
    if('ed_id' in request.GET):
        ed_id = request.GET['ed_id']
        mws_obj = Adv_word.objects.filter(id=ed_id).first()
        ed_en_word = mws_obj.en_word
        ed_jp_word = mws_obj.jp_word
        ed_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        en_word = request.POST['en_word']
        new_jp_word = request.POST['jp_word']
        mws_obj = Adv_word.objects.filter(en_word=en_word).first()
        mws_obj.jp_word = new_jp_word
        mws_obj.save()
        messages.success(request, '{0}を編集しました。'.format(en_word))

    params = {
        'ed_en_word':ed_en_word,
        'ed_jp_word':ed_jp_word,
        'ed_word_type':ed_word_type,
    }
    return render(request, 'mytoeic/adv_wordedit.html', params)

def in_wordedit(request):
    ed_en_word = ''
    ed_jp_word = ''
    ed_word_type = ''
    if('ed_id' in request.GET):
        ed_id = request.GET['ed_id']
        mws_obj = In_word.objects.filter(id=ed_id).first()
        ed_en_word = mws_obj.en_word
        ed_jp_word = mws_obj.jp_word
        ed_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        en_word = request.POST['en_word']
        new_jp_word = request.POST['jp_word']
        mws_obj = In_word.objects.filter(en_word=en_word).first()
        mws_obj.jp_word = new_jp_word
        mws_obj.save()
        messages.success(request, '{0}を編集しました。'.format(en_word))

    params = {
        'ed_en_word':ed_en_word,
        'ed_jp_word':ed_jp_word,
        'ed_word_type':ed_word_type,
    }
    return render(request, 'mytoeic/in_wordedit.html', params)

def other_wordedit(request):
    ed_en_word = ''
    ed_jp_word = ''
    ed_word_type = ''
    if('ed_id' in request.GET):
        ed_id = request.GET['ed_id']
        mws_obj = Other_word.objects.filter(id=ed_id).first()
        ed_en_word = mws_obj.en_word
        ed_jp_word = mws_obj.jp_word
        ed_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        en_word = request.POST['en_word']
        new_jp_word = request.POST['jp_word']
        mws_obj = Other_word.objects.filter(en_word=en_word).first()
        mws_obj.jp_word = new_jp_word
        mws_obj.save()
        messages.success(request, '{0}を編集しました。'.format(en_word))

    params = {
        'ed_en_word':ed_en_word,
        'ed_jp_word':ed_jp_word,
        'ed_word_type':ed_word_type,
    }
    return render(request, 'mytoeic/other_wordedit.html', params)

def memo_wordedit(request):
    ed_en_word = ''
    ed_jp_word = ''
    ed_word_type = ''
    if('ed_id' in request.GET):
        ed_id = request.GET['ed_id']
        mws_obj = Memo_word.objects.filter(id=ed_id).first()
        ed_en_word = mws_obj.en_word
        ed_jp_word = mws_obj.jp_word
        ed_word_type = mws_obj.word_type

    if(request.method == 'POST'):
        en_word = request.POST['en_word']
        new_jp_word = request.POST['jp_word']
        mws_obj = Memo_word.objects.filter(en_word=en_word).first()
        mws_obj.jp_word = new_jp_word
        mws_obj.save()
        messages.success(request, '{0}を編集しました。'.format(en_word))

    params = {
        'ed_en_word':ed_en_word,
        'ed_jp_word':ed_jp_word,
        'ed_word_type':ed_word_type,
    }
    return render(request, 'mytoeic/memo_wordedit.html', params)

#把py的渲染到html里面

#テーブルにデータを格納するための関数
# def insert_data(request):
    #in 詞をテーブルに追加
    # for data in t_all_w.in_words:
    #     try:
    #         jp_word = str(t_my_weblio.create_item(data[0]))
    #     except:
    #         jp_word = "no_explain"
            
    #     in_w = In_word(en_word=data[0], jp_word=jp_word, word_type=data[1])
    #     #import pdb; pdb.set_trace()#断点
    #     # n_w.update()
    #     in_w.save()
   
    # 動詞をテーブルに追加
    # for data in t_all_w.v_words:
    #     try:
    #         jp_word = str(t_my_weblio.create_item(data[0]))
    #     except:
    #         jp_word = "XXX_XXX_XXX"
            
    #     v_w = V_word(en_word=data[0], jp_word=jp_word, word_type=data[1])
    #     #import pdb; pdb.set_trace()#duandi
    #     # n_w.update()
    #     v_w.save()
    
    # #形容詞をテーブルに追加
    # for data in t_all_w.adj_words:
    #     try:
    #         jp_word = str(t_my_weblio.create_item(data[0]))
    #     except:
    #         jp_word = "XXX_XXX_XXX"
            
    #     adj_w = Adj_word(en_word=data[0], jp_word=jp_word, word_type=data[1])
    #     #import pdb; pdb.set_trace()#duandi
    #     # n_w.update()
    #     adj_w.save()
    
    # #副詞をテーブルに追加
    # for data in t_all_w.adv_words:
    #     try:
    #         jp_word = str(t_my_weblio.create_item(data[0]))
    #     except:
    #         jp_word = "XXX_XXX_XXX"
            
    #     adv_w = Adv_word(en_word=data[0], jp_word=jp_word, word_type=data[1])
    #     #import pdb; pdb.set_trace()#duandi
    #     # n_w.update()
    #     adv_w.save()
    
    # # #名詞類をテーブルに追加
    # for data in t_all_w.n_words:
    #     try:
    #         jp_word = str(t_my_weblio.create_item(data[0]))
    #     except:
    #         jp_word = "XXX_XXX_XXX"
            
    #     n_w = N_word(en_word=data[0], jp_word=jp_word, word_type=data[1])
    #     #import pdb; pdb.set_trace()#duandi
    #     # n_w.update()
    #     n_w.save()
    
    # # #他の詞をテーブルに追加
    # for data in t_all_w.other_words:
    #     try:
    #         jp_word = str(t_my_weblio.create_item(data[0]))
    #     except:
    #         jp_word = "XXX_XXX_XXX"
            
    #     other_w = Other_word(en_word=data[0], jp_word=jp_word, word_type=data[1])
    #     #import pdb; pdb.set_trace()#duandi
    #     # n_w.update()
    #     other_w.save()
        
    # return HttpResponse("ok")
    
        
        

