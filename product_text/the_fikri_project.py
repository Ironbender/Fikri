from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import nltk
import numpy as  np
from scipy import spatial



Product    = input("Hedef ürünün linkini giriniz...")
print(Product)

browser = webdriver.Chrome()
browser.get(Product)

print("deneme1")

pd_list= browser.find_element_by_id("feature-bullets")
print("deneme2")

product_description = []

items = pd_list.find_elements_by_tag_name("li")
for i in items:
    product_description.append(str(i.text))
    print("***")
    print(product_description)


'''
result  = nltk.word_tokenize(product_description[1])
result = nltk.pos_tag(result)
print("333")
print(result)
print("444*")
'''

for i in range(len(product_description)):
    product_description[i] = nltk.word_tokenize(product_description[i])
    product_description[i]=nltk.pos_tag(product_description[i])

print(product_description[2][1][1])
print(product_description)


def  feature_ext ( pd ):
    features = []
    for i in range(len(pd)):
        for j in range(len(pd[i])):
            if(len(pd[i][j])>1):
                if(str(pd[i][j][1])=='JJ' and str(pd[i][j+1][1])=='NN'):
                    features.append(str(pd[i][j][0]))
                    features.append(str(pd[i][j+1][0]))
                    features.append(str(pd[i][j][0]) + " " + str(pd[i][j+1][0]))

                if(str(pd[i][j][1])=='NNP' and str(pd[i][j+1][1])=='NNP' and str(pd[i][j+2][1])=='NNP'):
                    features.append(str(pd[i][j][0]) + " " + str(pd[i][j+1][0]) + " " + str(pd[i][j+2][0]) )

                #if(str(pd[i][j][1])=='NN' and str(pd[i][j+1][1])=='NN'):
                #    features.append(str(pd[i][j][0]) + " " + str(pd[i][j+1][0]) )    

                #if(str(pd[i][j][1])=='NN' and str(pd[i][j+1][1])=='NNS'):
                #    features.append(str(pd[i][j][0]) + " " + str(pd[i][j+1][0]) )    
                                          
    return features

product_features= []
product_features=feature_ext(product_description)
print(product_features)


embeddings_dict = {}

f = open('glove.6B.100d.txt', encoding='utf-8')

for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_dict[word] = coefs
f.close()
print(len(embeddings_dict))


def find_closest_embeddings(embedding):
    return sorted(embeddings_dict.keys(), key=lambda word: spatial.distance.euclidean(embeddings_dict[word], embedding))



def find_key_term(pf):    
    requirement = []
    requirement = pf
    key_term =[]
    be_split= []

    for i in range(len(requirement)):
        be_split = requirement[i].split()
        """
        if(int(len(be_split))==3):
            key_term [i]= find_closest_embeddings( embeddings_dict[ be_split[0]] + embeddings_dict[ be_split[1]] + embeddings_dict[ be_split[2]] )[:2]
        elif(  int(len(be_split)) ==2):
            key_term [i]= find_closest_embeddings( embeddings_dict[ be_split[0]] + embeddings_dict[ be_split[1]] )[:2]
        el
        """
        if( int(len(be_split))==1):
            key_term.append(find_closest_embeddings( embeddings_dict[ be_split[0]] )[:2])
    
    return key_term


key_word = find_key_term(product_features)
print(key_word)















