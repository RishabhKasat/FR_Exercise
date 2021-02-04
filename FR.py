# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:17:38 2021

@author: Rishabh
"""

stop_words=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

special_characters=['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
sentence_1=input("Enter the first sentence")
sentence_2=input("Enter the Second sentence")



#removing stop words from the sentences
def remove_stop_words(sentence):
    sent=[]
    for i in sentence.lower().strip().split():
        if i not in stop_words:
            for char in i:
                if char in special_characters:
                    i=i.replace(char,'')
        if len(i)>2:
            sent.append(i)
    return sent

bagofA=remove_stop_words(sentence_1)
bagofB=remove_stop_words(sentence_2)
vectorbag=set(bagofA).union(bagofB)


#converting words to numbers using conytervector
def countvec(bagofsent,vector):
    countv=[]
    wordict=dict.fromkeys(vectorbag,0)
    for i in bagofsent:
        wordict[i]+=1
    for i in wordict:
        countv.append(wordict[i])
    return countv

vector_a=countvec(bagofA, vectorbag)
vector_b=countvec(bagofB, vectorbag)

#Using cosing similarity for measurments
def cosine(vec_a,vec_b):
    sum_veca=0
    sum_vecb=0
    sum_vecab=0
    for i in range(len(vec_a)):
        sum_vecab+=(vec_a[i]*vec_b[i])
        sum_veca+=vec_a[i]**2
        sum_vecb+=vec_b[i]**2
    try:    
        result=(sum_vecab)/((sum_veca)**(1/2)*(sum_vecb)**(1/2))
    except:
        result=0
    
    return (result)

print("The similarity between two text is :",round(cosine(vector_a, vector_b),3))
