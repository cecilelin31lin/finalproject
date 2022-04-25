from nltk.corpus.reader import PlaintextCorpusReader
from nltk.probability import FreqDist

import urllib
file = urllib.request.urlopen(url="https://raw.githubusercontent.com/stopwords-iso/stopwords-zh/master/stopwords-zh.txt")
stopwords = file.read().decode("utf8").split()
#print(stopwords)

from string import printable
n = 300

Gossiping_dir = "Gossiping/May 27/"
pcr = PlaintextCorpusReader(root=Gossiping_dir, fileids=".*\.txt") #.*\. ??
fd = FreqDist(samples=pcr.words())
Gossiping_words = [word for word,freq in fd.most_common(n=n) if word not in stopwords and word[0] not in printable]

source_dir = "C_Chat/Sat May 15/"
pcr = PlaintextCorpusReader(root=source_dir, fileids=".*\.txt")
fd = FreqDist(samples=pcr.words())
C_Chat_words = [word for word,freq in fd.most_common(n=n) if word not in stopwords and word[0] not in printable]

print(Gossiping_dir)
print([word for word in Gossiping_words if word not in C_Chat_words])

print(source_dir)
print([word for word in C_Chat_words if word not in Gossiping_words])


# 1. What are the most common words in your two PTT boards respectively? 
#    Do they correspond to what you have expected?
#    (Please upload your Python script to GitHub, and paste your GitHub link on the online text of eCourse homework.)


from gensim.models import Word2Vec
from gensim.models.word2vec import PathLineSentences
corpus = PathLineSentences(Gossiping_dir)#"Gossiping")

model = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, workers=4)
print(model.wv.most_similar(positive=['女性',"老公"], negative=['男性']))

# 2. By using the GenSim Word2Vec module, 
#    find a word x in an analogy like "man : king :: woman : x" (read: man is to king as woman is to x) 
#    in your PTT texts.
#    (Please upload your Python script to GitHub, and paste your GitHub link on the online text of eCourse homework.)
