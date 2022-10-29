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

import mytoeic.all_words as t_all_w
import mytoeic.my_weblio as t_my_weblio

#引入模型
# Create your views here.
    
def index(request):
    return render(request, "mytoeic/index.html")

def n_wordlist(request):
    n_wordlist = N_word.objects.all()
    
    params = {
        'word':n_wordlist
    }
    
    return render(request, 'mytoeic/n_wordlist.html', params)

def v_wordlist(request):
    v_wordlist = V_word.objects.all()
    
    params = {
        'word':v_wordlist
    }
    
    return render(request, 'mytoeic/v_wordlist.html', params)

def adj_wordlist(request):
    adj_wordlist = Adj_word.objects.all()
    
    params = {
        'word':adj_wordlist
    }
    
    return render(request, 'mytoeic/adj_wordlist.html', params)

def adv_wordlist(request):
    adv_wordlist = Adv_word.objects.all()
    
    params = {
        'word':adv_wordlist
    }
    
    return render(request, 'mytoeic/adv_wordlist.html', params)

def in_wordlist(request):
    in_wordlist = In_word.objects.all()
    
    params = {
        'word':in_wordlist
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
    
        
        

