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
from nltk.corpus import wordnet as wn

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

sen3 = " Apple skin contains the flavonoid quercetin, which can help regulate the immune system and reduce inflammation. "

print(find_closest_embeddings( embeddings_dict["apple"] + embeddings_dict["skinn"])[:20] )


"""
print(find_closest_embeddings( embeddings_dict["apple"])[:10] )
print(find_closest_embeddings( embeddings_dict["skinn"])[:10] )
print(find_closest_embeddings( embeddings_dict["fruit"])[:10] )
print(find_closest_embeddings( embeddings_dict["contains"])[:10] )
print(find_closest_embeddings( embeddings_dict["flavonoid"])[:10] )
print(find_closest_embeddings( embeddings_dict["quercetin"])[:10] )
print(find_closest_embeddings( embeddings_dict["regulate"])[:10] )
print(find_closest_embeddings( embeddings_dict["immune"])[:10] )
"""

sen4 = "Precision Tare Button calculates the net weight of your ingredients by automatically subtracting the weight of any bowl or container."

sen5 = "Runs on 2 AAA batteries (included) that automatically power-off after 2-minutes to preserve battery life, and an easy-access battery compartment (no screwdriver needed). Satisfaction Guaranteed."

sen6 = "Features a newly enlarged weighing platform finished in elegant chrome, and 2 large buttons that generate an audible click confirmation. Cleans and stores easily."







