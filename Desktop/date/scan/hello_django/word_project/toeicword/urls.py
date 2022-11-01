from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),#toppageのURL
    #"view.pyで関数を定義したら、URLを対応付けさせる"
    path('wordlist/', views.wordlist, name='wordlist'),#追加部：単語リストページのURL
    path('wordregistration', views.wordregistration, name="wordregistration"),
    path('worddelete/', views.worddelete, name="worddelete"),
    path('wordedit/', views.wordedit, name="wordedit"),
    path('answer/', views.answer, name='answer'),
]

"""
path(引数1, 引数2, 引数3)

引数1：アドレスバーに表示されるURLの指定を行います。
引数2：views.pyで定義した関数名を指定します。
引数3：「name=’●●●’」でURLに名前付けを行います。

例：toeicword/urls.pyで設定したpath('', views.index, name=’index’)の場合、
URLは「http://localhost:8000/flashcard/」 
このURLをプログラム上で呼び出すには「index」と書く。
"""


