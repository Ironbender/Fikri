import numpy as np
import pandas as pd
import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
stop_words=stopwords.words('english')
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

C0 = 'Premium Material: The bands for apple watch are made of durable and soft silicone, prevents skin from irritation; flexible, lightweight and very comfortable to wear. Sweat & water resistant.'
C1 = 'Multi Choices: Various colors and two selected sizes for you to choose, personalize your apple watch to fit your mood and outfit in daily life, dress up your Watch and highlight your unique taste. Pin-and-tuck closure ensures a clean fit.'
C2 = 'Easy Installation and Removal: The band for Watch comes with watch lugs on both ends, which locks onto 2018 Watch interface precisely. Easy and direct installation and one button removal.'
C3 = 'Lifetime Customer Service: Please contact us at once if any quality problem, we provide lifetime customer service and will resolve for you within 24 hours.'

C0=C0.split()
C1=C1.split()
C2=C2.split()
C3=C3.split()

print(C3)
    







