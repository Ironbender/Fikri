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



words = ['amazing', 'love', 'great', 'nice']

for w in words:
    tmp = wn.synsets(w)[0].pos()
    print( w, ":", tmp)

































