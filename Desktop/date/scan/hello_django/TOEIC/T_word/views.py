from venv import create
from django.shortcuts import render
from django.http import HttpResponse

from .models import N_word #追加部
from .models import V_word
from .models import Adj_word
from .models import Adv_word
from .models import In_word
from .models import Other_word

import T_word.all_words as t_all_w
import T_word.my_weblio as t_my_weblio

#引入模型
# Create your views here.
def index(request):
    return HttpResponse("hello!")
    
def insert_data(request):
    #in 詞をテーブルに追加
    # for data in t_all_w.in_words:
    #     try:
    #         jp_word = str(t_my_weblio.create_item(data[0]))
    #     except:
    #         jp_word = "no_explain"
            
    #     in_w = In_word(en_word=data[0], jp_word=jp_word, word_type=data[1])
    #     #import pdb; pdb.set_trace()#duandi
    #     # n_w.update()
    #     in_w.save()
   
    # # 動詞をテーブルに追加
    # for data in t_all_w.v_words:
    #     try:
    #         jp_word = str(t_my_weblio.create_item(data[0]))
    #     except:
    #         jp_word = "XXX_XXX_XXX"
            
    #     v_w = V_word(en_word=data[0], jp_word=jp_word, word_type=data[1])
    #     #import pdb; pdb.set_trace()#duandi
    #     # n_w.update()
    #     v_w.save()
    
    #形容詞をテーブルに追加
    for data in t_all_w.adj_words:
        try:
            jp_word = str(t_my_weblio.create_item(data[0]))
        except:
            jp_word = "XXX_XXX_XXX"
            
        adj_w = Adj_word(en_word=data[0], jp_word=jp_word, word_type=data[1])
        #import pdb; pdb.set_trace()#duandi
        # n_w.update()
        adj_w.save()
    
    # #副詞をテーブルに追加
    for data in t_all_w.adv_words:
        try:
            jp_word = str(t_my_weblio.create_item(data[0]))
        except:
            jp_word = "XXX_XXX_XXX"
            
        adv_w = Adv_word(en_word=data[0], jp_word=jp_word, word_type=data[1])
        #import pdb; pdb.set_trace()#duandi
        # n_w.update()
        adv_w.save()
    
    # #名詞類をテーブルに追加
    for data in t_all_w.n_words:
        try:
            jp_word = str(t_my_weblio.create_item(data[0]))
        except:
            jp_word = "XXX_XXX_XXX"
            
        n_w = N_word(en_word=data[0], jp_word=jp_word, word_type=data[1])
        #import pdb; pdb.set_trace()#duandi
        # n_w.update()
        n_w.save()
    
    # #他の詞をテーブルに追加
    for data in t_all_w.other_words:
        try:
            jp_word = str(t_my_weblio.create_item(data[0]))
        except:
            jp_word = "XXX_XXX_XXX"
            
        other_w = Other_word(en_word=data[0], jp_word=jp_word, word_type=data[1])
        #import pdb; pdb.set_trace()#duandi
        # n_w.update()
        other_w.save()
        
    return HttpResponse("ok")
    
        
        

