
from nltk import word_tokenize, pos_tag
import string
import re

from collections import Counter
import math

with open('T1-1-all.txt', encoding='UTF-8') as file_1:
    str_e = file_1.read()
    
    str_e_list = word_tokenize(str_e)#すべての英文を単語にする
    
    # print("英単語：" + ",".join(str_e_list))
    #print(str_e_list)
    # for i in str_e_list:
    #     if i.isalpha() == False:
    #         str_e_list.strip(i)
    #str_e_no_punc = ' '.join([i for i in str_e_list if i not in string.punctuation])#部分読点が削除できない例「'」
    
    str_e_no_punc = re.findall(r'\b\w+\b', str_e)#すべての読点が削除でき、リストになる
    #print(str_e)文書
    #print(str_e_no_punc)#すべての単語が入ってる一次リスト
    
    
   
#key:リスト要素,　value:リスト要素の個数



#データ処理：二次リストword_listを作る
def data_process(data):
    words_list = list()
    for i in range(len(data)):
        sep = data[i].split(' ')#一つ一つの単語が入るリストを作る
        words_list.append(sep)#二次リストになる
    return words_list

#単語を数える
def count_words(words_list):
    count_list = list()
    for i in range(len(words_list)):#4回ループする
        count = Counter(words_list[i])#インデックスi中の各単語の個数を数えて、count_listを作る
        count_list.append(count)
        #print("\n", "count", count, "\n")
    return count_list

def tf(word, count):#ある単語の出現頻度/すべての単語の出現頻度の総和
    return count[word] / sum(count.values())#一つの文書内の単語の個数割るすべての単語の個数の総和

def idf(word, count_list):#文書総数/この単語を含む文書数
    t_in_text = sum([1 for count in count_list if word in count])#ある単語を含む文書数を総和を求める
    #print("<<<<<<<<<<", t_in_text, count)
    #print(t_in_text)
    return math.log(len(count_list) / (1 + t_in_text))#

                    
def tf_idf(word, count, count_list):
    #print("wwwwwwwwww", word, count)
    return tf(word, count) * idf(word, count_list)


words_list = data_process(str_e_no_punc)
count_list = count_words(words_list)

#print("!!!!!!!!!!", words_list, "\n")#一つの単語が一つリストになって、大きいに二次リストになってる
#print("##########", count_list, len(count_list), "\n")#Counter({単語：１})のような形が入ってるリスト、最後に

for i, count in enumerate(count_list):
    #print("&&&&&&&&&&", i+1, count)
    w1 = f"The tf-idf of the {i+1} document:"
    #print(w1)
    scores = {word: tf_idf(word, count, count_list) for word in count}#TF-IDFを計算する
    #sort_scores = sorted(scores.items(), key=lambda x:x[1], reverse=True)
    #print(sort_scores)
    dic2 = sorted(scores.items(), key=lambda x:x[1])
    print(dic2)#一つの文書内の単語と対応するTF-IDFの値をプリントする
    

    