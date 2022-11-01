#%%
import re 
from collections import Counter
import math

#定数
FILE = ['T1-1-all.txt', 'T1-2-all.txt']

def read_file(file):
    with open(file, encoding='UTF-8') as f:
        f_read = f.read().lower()
        #print(f_read)
        str_nopunc = re.findall(r'\b\w+\b', f_read)#すべての読点が削除でき、リストになる
        #一つの文書内のデータ処理：リスト内の重複要素の数を数え、要素をキーに、数をvalueにして、辞書を作成
        str_dic = dict(Counter(str_nopunc))
        #return str_dic#単語と各単語の個数が入ってる辞書
        # print(str_dic)
        return str_dic#文書
        #print(str_no_punc)#すべての単語が入ってる一次リスト
        

def tf(word, str_dic):##ある単語の出現頻度/すべての単語の出現頻度の総和
    #print(word, str_dic[word], sum(str_dic.values()))
    tf_v = str_dic[word] / sum(str_dic.values())
    # print("book", str_dic["book"], sum(str_dic.values()))
    #print(tf_v)
    return tf_v

# def idf(word, count_list):#文書総数/この単語を含む文書数
#     #t_in_text = sum([1 for count in count_list if word in count])#ある単語を含む文書数を総和を求める
#     s = 0
#     for count in count_list:
#         if word in count:
#             s += 1
#             idf_v =  math.log(len(FILE) / (s))
#             #print(word, s, len(FILE), format(math.log(len(FILE))/(1+s), ".04"))
#     return idf_v


def idf(word, count_list):#文書総数/この単語を含む文書数
    #t_in_text = sum([1 for count in count_list if word in count])#ある単語を含む文書数を総和を求める
    t_in_text = sum([1 for count in count_list if word in count])#ある単語を含む文書数を総和を求める
    # print(word, t_in_text)
    idf_v =  math.log(len(FILE) / (t_in_text+1))
            #print(word, s, len(FILE), format(math.log(len(FILE))/(1+s), ".04"))
    return idf_v

def tf_idf(word, str_dic, count_list):
    tf_idf_v = tf(word, str_dic) * idf(word, count_list)
    print("wwwwwwwwww", word, tf_idf_v)
    return tf_idf_v

def main():
    count_list = []
    for file in FILE:
        str_dic = read_file(file)#辞書
        count_list.append(str_dic)
        
        #print("!!!!!!str_dic", str_dic)
        #print("??????count_list", count_list)
        #scores = {word: tf_idf(word, str_dic, count_list) for word in str_dic}#TF-IDFを計算する
        # dic2 = sorted(scores.items(), key=lambda x:x[1])
        # #sort_scores = sorted(scores.items(), key=lambda x:x[1], reverse=True)#降順
    #    print(scores)
    #print(count_list)
    for i, count in enumerate(count_list, 1):
        print(f"This is the {i} document.")
        for word in count:
    #         tf_v = tf(word, count)
    #         idf_v = idf(word, count_list)
    #         #print(tf_v)
        #scores = {word: tf_idf(word, count, count_list) for word in count}#TF-IDFを計算する    
            tf_idf_v = tf_idf(word, count, count_list)
            #print(word, tf_idf_v)
            
            
main()
# for i in FILE:
#     print("!!!!!!!!!!!!!!!!!!", "\n")
#     str_dic = read_file(i)
    
# %%
