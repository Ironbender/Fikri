# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import numpy as np
import pandas as pd
import nltk
import re
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx




'''
# data
df=pd.DataFrame({'x': range(1,10), 'y': np.random.randn(9)*80+range(1,10) })
 
# plot
plt.plot( 'x', 'y', data=df, linestyle='-', marker='o')
plt.show()

'''
C0 = 'Premium Material: The bands for apple watch are made of durable and soft silicone, prevents skin from irritation; flexible, lightweight and very comfortable to wear. Sweat & water resistant.'
C1 = 'Multi Choices: Various colors and two selected sizes for you to choose, personalize your apple watch to fit your mood and outfit in daily life, dress up your Watch and highlight your unique taste. Pin-and-tuck closure ensures a clean fit.'
C2 = 'Easy Installation and Removal: The band for Watch comes with watch lugs on both ends, which locks onto 2018 Watch interface precisely. Easy and direct installation and one button removal.'
C3 = 'Lifetime Customer Service: Please contact us at once if any quality problem, we provide lifetime customer service and will resolve for you within 24 hours.'

C0=C0.split()
C1=C1.split()
C2=C2.split()
C3=C3.split()

a = []
a = len(C3)


df = pd.DataFrame({'x':range(1,a), 'y':np.random.randn(a-1)*150 + range(1,a) } )

plt.plot('x','y',data=df,linestyle='-',marker='o')
plt.show()


def word_connection ( sentence , index):
    


    return sentence


def sentence_connection( sentence):
    connected_sentence = []



    return connected_sentence


def product_feautres(sentence):
    features_list = []


    return features_list


def features_benefit (features_list , sentence):
    benefit_list = []


    return benefit_list












