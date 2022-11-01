from django import forms#フォームを作るには必要なもの

class RegistrationForm(forms.Form):#「forms.form」を継承してクラスの宣言を行う
    #英単語を代入する変数
    en_word = forms.CharField(label="English", max_length=200)
    #日本語を代入する変数
    jp_word = forms.CharField(label="日本語", max_length=200)
    #「forms.CharField」は文字列を変数に代入させるための物である。
    #「label」はフォームをブラウザに表示する時に使う、
    #変数がどのような物であるかを表す物である。
    