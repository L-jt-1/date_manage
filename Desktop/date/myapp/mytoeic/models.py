from django.db import models
# import logging
# import sys

# Create your models here.
#すべての品詞の種類
#名詞類６：NNP固有名詞, NN名詞, PRP人称代名詞 (PP),WP Wh 代名詞、WP$所有 Wh 代名詞, NNS名詞 (複数形), 
# 動詞類１： VB動詞 (原形),
#形容詞類３：JJ形容詞,  JJR形容詞 (比較級),  JJS形容詞 (最上級),  
#副詞類４： RB副詞,RBR副詞 (比較級),RBS副詞 (最上級), WRB Wh 副詞,
# IN前置詞または従属接続詞類１：  
#他の品詞８：PDT前限定辞,CC調整接続詞, CD基数,FW外国語,DT限定詞, , RP不変化詞, UH感嘆詞, MD法 情态动词


#名詞：NN,NNP,
class N_word(models.Model):
    id = models.AutoField(primary_key=True)
#     #idは通し番号として利用する。
#「AutoField」はユーザが特に操作しなくても格納されるフィールド
    #「primary_key」はその行を一意に決めるための物である。
    en_word = models.CharField(max_length=200, unique=True)
    #英単語を格納するため、「CharField」は文字列を格納時に使う
    #「max_length」は文字列の長さの最大値を決めるための物
    #「unique」は同じ英単語を格納しないようにするための物
    jp_word = models.CharField(max_length=200)
    #日本語約を格納するために使う
    word_type = models.CharField(max_length=200)
    def __str__(self):#django　adminで確認する時に表示されるデータを指示する
        return self.en_word

#動詞：VB動詞 (原形)
#class 所有首字母大写，VWord
class V_word(models.Model):
    id = models.AutoField(primary_key=True)
#     #idは通し番号として利用する。
#「AutoField」はユーザが特に操作しなくても格納されるフィールド
    #「primary_key」はその行を一意に決めるための物である。
    en_word = models.CharField(max_length=200, unique=True)
    #英単語を格納するため、「CharField」は文字列を格納時に使う
    #「max_length」は文字列の長さの最大値を決めるための物
    #「unique」は同じ英単語を格納しないようにするための物
    jp_word = models.CharField(max_length=200)
    word_type = models.CharField(max_length=200)
    #日本語約を格納するために使う
    def __str__(self):#django　adminで確認する時に表示されるデータを指示する
        return self.en_word
    
#形容詞：JJ,JJR比較級,JJS最高級
#!!!!!!!!!!!!ADJWord
class Adj_word(models.Model):
    id = models.AutoField(primary_key=True)
#     #idは通し番号として利用する。
#「AutoField」はユーザが特に操作しなくても格納されるフィールド
    #「primary_key」はその行を一意に決めるための物である。
    en_word = models.CharField(max_length=200, unique=True)
    #英単語を格納するため、「CharField」は文字列を格納時に使う
    #「max_length」は文字列の長さの最大値を決めるための物
    #「unique」は同じ英単語を格納しないようにするための物
    jp_word = models.CharField(max_length=200)
    #日本語約を格納するために使う
    word_type = models.CharField(max_length=200)
    def __str__(self):#django　adminで確認する時に表示されるデータを指示する
        return self.en_word
#副詞：RB,
class Adv_word(models.Model):
    id = models.AutoField(primary_key=True)
#     #idは通し番号として利用する。
#「AutoField」はユーザが特に操作しなくても格納されるフィールド
    #「primary_key」はその行を一意に決めるための物である。
    en_word = models.CharField(max_length=200, unique=True)
    #英単語を格納するため、「CharField」は文字列を格納時に使う
    #「max_length」は文字列の長さの最大値を決めるための物
    #「unique」は同じ英単語を格納しないようにするための物
    jp_word = models.CharField(max_length=200)
    word_type = models.CharField(max_length=200)
    #日本語約を格納するために使う
    def __str__(self):#django　adminで確認する時に表示されるデータを指示する
        return self.en_word
    
#IN前置詞または従属接続詞
class In_word(models.Model):
    id = models.AutoField(primary_key=True)
#     #idは通し番号として利用する。
#「AutoField」はユーザが特に操作しなくても格納されるフィールド
    #「primary_key」はその行を一意に決めるための物である。
    en_word = models.CharField(max_length=200, unique=True)
    #英単語を格納するため、「CharField」は文字列を格納時に使う
    #「max_length」は文字列の長さの最大値を決めるための物
    #「unique」は同じ英単語を格納しないようにするための物
    jp_word = models.CharField(max_length=200)
    word_type = models.CharField(max_length=200)
    #日本語約を格納するために使う
    def __str__(self):#django　adminで確認する時に表示されるデータを指示する
        return self.en_word

#其他
class Other_word(models.Model):
    id = models.AutoField(primary_key=True)
#     #idは通し番号として利用する。
#「AutoField」はユーザが特に操作しなくても格納されるフィールド
    #「primary_key」はその行を一意に決めるための物である。
    en_word = models.CharField(max_length=200, unique=True)
    #英単語を格納するため、「CharField」は文字列を格納時に使う
    #「max_length」は文字列の長さの最大値を決めるための物
    #「unique」は同じ英単語を格納しないようにするための物
    jp_word = models.CharField(max_length=200)
    word_type = models.CharField(max_length=200)
    #日本語約を格納するために使う
    def __str__(self):#django　adminで確認する時に表示されるデータを指示する
        return self.en_word
    
#メモ帳
class Memo_word(models.Model):
    id = models.AutoField(primary_key=True)
#     #idは通し番号として利用する。
#「AutoField」はユーザが特に操作しなくても格納されるフィールド
    #「primary_key」はその行を一意に決めるための物である。
    en_word = models.CharField(max_length=200, unique=True)
    #英単語を格納するため、「CharField」は文字列を格納時に使う
    #「max_length」は文字列の長さの最大値を決めるための物
    #「unique」は同じ英単語を格納しないようにするための物
    jp_word = models.CharField(max_length=200)
    word_type = models.CharField(max_length=200)
    #日本語約を格納するために使う
    def __str__(self):#django　adminで確認する時に表示されるデータを指示する
        return self.en_word
    

