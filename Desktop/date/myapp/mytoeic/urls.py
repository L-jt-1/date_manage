from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('insert_data/', views.insert_data, name="insert_data")
    path('n_wordlist/', views.n_wordlist, name='n_wordlist'),
    path('v_wordlist/', views.v_wordlist, name='v_wordlist'),
    path('adj_wordlist/', views.adj_wordlist, name='adj_wordlist'),
    path('adv_wordlist/', views.adv_wordlist, name='adv_wordlist'),
    path('in_wordlist/', views.in_wordlist, name='in_wordlist'),
    path('other_wordlist/', views.other_wordlist, name='other_wordlist'),
]