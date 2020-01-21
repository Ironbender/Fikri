import numpy as np
import pandas as pd
import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx


##  Product Description sentence
ProDes = "Easy Blending Cycles: one-touch buttons, six pre-programmed cycles, pulse, and ten speed manual control with the ability to achieve a variety of textures. Complete control to adjust your blending at any time"

ProDes = ProDes.split()
print(ProDes)

f =open('glove.6B.100d.txt',encoding='utf-8')

word_embeddings = {}

for line in f:
  values = line.split()
  word = values[0]
  coefs = np.asarray(values[1:],dtype='float32')
  word_embeddings[word] = coefs
f.close()

print(len(word_embeddings))



### -> vector description


word_vector = []

for i in ProDes:
  if len(i) != 0:
    v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()])/(len(i.split())+0.001)
  else:
    v = np.zeros((100,))
  word_vector.append(v)

##print(word_vector)


### -> similarity matrix description

sim_mat = np.zeros([len(ProDes), len(ProDes)])

for i in range(len(ProDes)):
  for j in range(len(ProDes)):
    if i != j:
      sim_mat[i][j] = cosine_similarity(word_vector[i].reshape(1,100), word_vector[j].reshape(1,100))[0,0]


print(sim_mat)

nx_graph = nx.from_numpy_array(sim_mat)
scores = nx.pagerank(nx_graph)

ranked_word = sorted(((scores[i],s) for i,s in enumerate(ProDes)), reverse=True)

for i in range(10):
  print(ranked_word[i][1])


'''

CleanSentence = pd.Series(ProDes).str.replace("[^a-zA-Z]"," ")
CleanSentence = [s.lower() for s in CleanSentence]

print(CleanSentence)

# function to remove stopwords
def remove_stopwords(sen):
    sen_new = " ".join([i for i in sen if i not in stop_words])
    return sen_new

Words = []

for s in CleanSentence:
  Words.append(sent_tokenize(s))

Words = [y for x in Words for y in x] # flatten list

print(Words[0])
'''


