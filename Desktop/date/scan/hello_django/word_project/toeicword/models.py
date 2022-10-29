from django.db import models

# Create your models here.
class MyWord(models.Model):#テーブル名はMyWord
    id = models.AutoField(primary_key=True)
    #idは通し番号として利用する。
    # 「AutoField」はユーザが特に操作しなくても格納されるフィールド
    #「primary_key」はその行を一意に決めるための物である。
    en_word = models.CharField(max_length=200, unique=True)
    #英単語を格納するため、「CharField」は文字列を格納時に使う
    #「max_length」は文字列の長さの最大値を決めるための物
    #「unique」は同じ英単語を格納しないようにするための物
    jp_word = models.CharField(max_length=200)
    #日本語約を格納するために使う
    def __str__(self):#django　adminで確認する時に表示されるデータを指示する
        return self.en_word

#すべての品詞の種類
#NNP固有名詞, WP$所有 Wh 代名詞, CC調整接続詞, JJS形容詞 (最上級), PRP人称代名詞 (PP), 
# PDT前限定辞, RBR副詞 (比較級), RB副詞, JJR形容詞 (比較級), FW外国語, 
# JJ形容詞, RBS副詞 (最上級), CD基数, NN名詞, IN前置詞または従属接続詞, NNS名詞 (複数形), 
# VB動詞 (原形), WRB Wh 副詞, DT限定詞, WP Wh 代名詞, RP不変化詞, UH感嘆詞, MD法 情态动词

# N_word = {('november', 'NNP'): 3, ('october', 'NNP'): 2, ('subscriber', 'NNP'): 2, 
#           ('meet', 'NNP'): 2, ('mail', 'NNP'): 1, ('heard', 'NNP'): 1, ('jason', 'NNP'): 1,
#           ('know', 'NNP'): 1, ('bulletin', 'NNP'): 1, ('xia', 'NNP'): 1, ('kirkland', 'NNP'): 1,
#           ('web', 'NNP'): 1, ('mat', 'NNP'): 1, ('yang', 'NNP'): 1, ('kitchen', 'NNP'): 1,
#           ('september', 'NNP'): 1, ('trouser', 'NNP'): 1}
# #名詞：
# class N_word(models.Model):
#     id = models.AutoField(primary_key=True)
# #     #idは通し番号として利用する。
# #「AutoField」はユーザが特に操作しなくても格納されるフィールド
#     #「primary_key」はその行を一意に決めるための物である。
#     en_word = models.CharField(max_length=200, unique=True)
#     #英単語を格納するため、「CharField」は文字列を格納時に使う
#     #「max_length」は文字列の長さの最大値を決めるための物
#     #「unique」は同じ英単語を格納しないようにするための物
#     jp_word = models.CharField(max_length=200)
#     #日本語約を格納するために使う
#     def __str__(self):#django　adminで確認する時に表示されるデータを指示する
#         return self.en_word

# #名詞：NN,NNP,
# class V_word(models.Model):
#     id = models.AutoField(primary_key=True)
# #     #idは通し番号として利用する。
# #「AutoField」はユーザが特に操作しなくても格納されるフィールド
#     #「primary_key」はその行を一意に決めるための物である。
#     en_word = models.CharField(max_length=200, unique=True)
#     #英単語を格納するため、「CharField」は文字列を格納時に使う
#     #「max_length」は文字列の長さの最大値を決めるための物
#     #「unique」は同じ英単語を格納しないようにするための物
#     jp_word = models.CharField(max_length=200)
#     #日本語約を格納するために使う
#     def __str__(self):#django　adminで確認する時に表示されるデータを指示する
#         return self.en_word
    
# #形容詞：JJ,JJR比較級,JJS最高級
# class Adj_word(models.Model):
#     id = models.AutoField(primary_key=True)
# #     #idは通し番号として利用する。
# #「AutoField」はユーザが特に操作しなくても格納されるフィールド
#     #「primary_key」はその行を一意に決めるための物である。
#     en_word = models.CharField(max_length=200, unique=True)
#     #英単語を格納するため、「CharField」は文字列を格納時に使う
#     #「max_length」は文字列の長さの最大値を決めるための物
#     #「unique」は同じ英単語を格納しないようにするための物
#     jp_word = models.CharField(max_length=200)
#     #日本語約を格納するために使う
#     def __str__(self):#django　adminで確認する時に表示されるデータを指示する
#         return self.en_word
# #副詞：RB,
# class Adv_word(models.Model):
#     id = models.AutoField(primary_key=True)
# #     #idは通し番号として利用する。
# #「AutoField」はユーザが特に操作しなくても格納されるフィールド
#     #「primary_key」はその行を一意に決めるための物である。
#     en_word = models.CharField(max_length=200, unique=True)
#     #英単語を格納するため、「CharField」は文字列を格納時に使う
#     #「max_length」は文字列の長さの最大値を決めるための物
#     #「unique」は同じ英単語を格納しないようにするための物
#     jp_word = models.CharField(max_length=200)
#     #日本語約を格納するために使う
#     def __str__(self):#django　adminで確認する時に表示されるデータを指示する
#         return self.en_word
    
# #N前置詞または従属接続詞
# class Adv_word(models.Model):
#     id = models.AutoField(primary_key=True)
# #     #idは通し番号として利用する。
# #「AutoField」はユーザが特に操作しなくても格納されるフィールド
#     #「primary_key」はその行を一意に決めるための物である。
#     en_word = models.CharField(max_length=200, unique=True)
#     #英単語を格納するため、「CharField」は文字列を格納時に使う
#     #「max_length」は文字列の長さの最大値を決めるための物
#     #「unique」は同じ英単語を格納しないようにするための物
#     jp_word = models.CharField(max_length=200)
#     #日本語約を格納するために使う
#     def __str__(self):#django　adminで確認する時に表示されるデータを指示する
#         return self.en_word

# #其他
# class Adv_word(models.Model):
#     id = models.AutoField(primary_key=True)
# #     #idは通し番号として利用する。
# #「AutoField」はユーザが特に操作しなくても格納されるフィールド
#     #「primary_key」はその行を一意に決めるための物である。
#     en_word = models.CharField(max_length=200, unique=True)
#     #英単語を格納するため、「CharField」は文字列を格納時に使う
#     #「max_length」は文字列の長さの最大値を決めるための物
#     #「unique」は同じ英単語を格納しないようにするための物
#     jp_word = models.CharField(max_length=200)
#     #日本語約を格納するために使う
#     def __str__(self):#django　adminで確認する時に表示されるデータを指示する
#         return self.en_word
    

