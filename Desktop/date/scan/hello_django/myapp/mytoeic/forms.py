from django import forms

# Create your forms hear.
#フォームとは、ユーザから入力を受ける部分のことを指します。
class RegistrationForm(forms.Form):
    en_word = forms.CharField(label='English', max_length=200)
    jp_word = forms.CharField(label='日本語', max_length=200)
    word_type = forms.CharField(label="品詞", max_length=200)