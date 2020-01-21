import nltk

text = 'Easy strapping and light weight feature are added to this mat for easy Transport and storage. '
text2 = 'BalanceFrom all-purpose premium exercise yoga mat is manufactured and sold exclusively by BalanceFrom Amazon store'
text = nltk.word_tokenize(text)
text2 = nltk.word_tokenize(text2)

r2 = nltk.pos_tag(text2)
result = nltk.pos_tag(text)
print(result)
print(r2)

"""
result = [i for i in result if i[0].lower() == 'table']

print(result) # [('table', 'JJ'), ('table', 'VB'), ('table', 'NN')]
"""







