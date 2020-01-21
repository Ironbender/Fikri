import numpy as np
import pandas as pd
import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from scipy import spatial
from sklearn.manifold import TSNE


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

print(find_closest_embeddings(embeddings_dict["apple"] -embeddings_dict["computer"] + embeddings_dict["fruit"])[:5] )


prodes = "ULTRA-FAST READ WRITE SPEEDS: Up to 100MB/s read and 90MB/s write speeds; UHS Speed Class U3 and Speed Class 10 (performance may vary based on host device, interface, usage conditions, and other factors)"

prodes = prodes.split()

sen1 = "apple is very healty fruit"
sen2 = "Apples May Be Good for Your Heart "
sen3 = " Apple skin contains the flavonoid quercetin, which can help regulate the immune system and reduce inflammation. "


sen1 = sen1.split()
for i in range(sen1):
    
    




 





