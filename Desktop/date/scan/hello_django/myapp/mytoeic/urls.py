from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('insert_data/', views.insert_data, name="insert_data")
    #品詞語との単語リストページ
    path('n_wordlist/', views.n_wordlist, name='n_wordlist'),
    path('v_wordlist/', views.v_wordlist, name='v_wordlist'),
    path('adj_wordlist/', views.adj_wordlist, name='adj_wordlist'),
    path('adv_wordlist/', views.adv_wordlist, name='adv_wordlist'),
    path('in_wordlist/', views.in_wordlist, name='in_wordlist'),
    path('other_wordlist/', views.other_wordlist, name='other_wordlist'),
    path('memo_wordlist/', views.memo_wordlist, name='memo_wordlist'),
    path('wordregistration/', views.wordregistration, name="wordregistration"),
    #単語削除ページ
    path('n_worddelete/', views.n_worddelete, name="n_worddelete"),
    path('v_worddelete/', views.v_worddelete, name="v_worddelete"),
    path('adj_worddelete/', views.adj_worddelete, name="adj_worddelete"),
    path('adv_worddelete/', views.adv_worddelete, name="adv_worddelete"),
    path('in_worddelete/', views.in_worddelete, name="in_worddelete"),
    path('other_worddelete/', views.other_worddelete, name="other_worddelete"),
    path('memo_worddelete/', views.memo_worddelete, name="memo_worddelete"),
    #単語編集
    path('n_wordedit/', views.n_wordedit, name="n_wordedit"),
    path('v_wordedit/', views.v_wordedit, name="v_wordedit"),
    path('adj_wordedit/', views.adj_wordedit, name="adj_wordedit"),
    path('adv_wordedit/', views.adv_wordedit, name="adv_wordedit"),
    path('in_wordedit/', views.in_wordedit, name="in_wordedit"),
    path('other_wordedit/', views.other_wordedit, name="other_wordedit"),
    path('memo_wordedit/', views.memo_wordedit, name="memo_wordedit"),
]