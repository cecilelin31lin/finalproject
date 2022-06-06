from nltk.corpus.reader import PlaintextCorpusReader
from nltk.probability import FreqDist
import random


n = 200

D_dir = "/Users/lin/Desktop/final project/DISC/D"
pcr1 = PlaintextCorpusReader(root=D_dir, fileids=".*\.txt") 
#.*\ 是所有檔案的意思

c = "D"
D_documents = [(pcr1.words(fileid),c) for fileid in pcr1.fileids()]
#print(Gossiping_documents[:9])

I_dir = "/Users/lin/Desktop/final project/DISC/I"
pcr2 = PlaintextCorpusReader(root=I_dir, fileids=".*\.txt")

c = "I"
I_documents = [(pcr2.words(fileid),c) for fileid in pcr2.fileids()]

S_dir = "/Users/lin/Desktop/final project/DISC/S"
pcr1 = PlaintextCorpusReader(root=S_dir, fileids=".*\.txt") 
#.*\ 是所有檔案的意思

c = "S"
S_documents = [(pcr1.words(fileid),c) for fileid in pcr1.fileids()]
#print(Gossiping_documents[:9])

C_dir = "/Users/lin/Desktop/final project/DISC/I"
pcr2 = PlaintextCorpusReader(root=C_dir, fileids=".*\.txt")

c = "C"
C_documents = [(pcr2.words(fileid),c) for fileid in pcr2.fileids()]
#(pcr2.words(fileid),c) 是 tuple
#word definition 裡的self是甚麼意思??
#print(C_Chat_documents[:9]) #印出 sat may那一個資料夾的，因為 C_Chat_dir = "C_Chat/Sat May 15/"


documents = D_documents + I_documents + S_documents + C_documents
#documents就變成一個list裡面裝超多g/c list
#print(documents[0])
#print(documents[-1]) #印出documents的最後一個元素

random.shuffle(x=documents) 
# Different results each time? same; otherwise, the random.seed() is required

import datetime
#print(datetime.datetime.now())

N_features = 180
all_words = FreqDist(pcr1.words() + pcr2.words())   # 20 seconds...??
#print(all_words)#<FreqDist with 33003 samples and 530403 outcomes>
#all_words只是物件，只會印出資訊
word_features = list(all_words)[:N_features] 
#出現頻率最高的0-1999(N_features)個字
#word_features會把all_words變成list，就可以印出一堆東西
#print(word_features) #[':', '/', '.', '05', '推', '→', '24', '23', '，', '的', '了', '是', '有', '-', '？', '噓....

def document_features(document_words):
    document_words = set(document_words)
    #在資料結構上有排序，找東西比較快。所以是可以用list的。
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words) #是簡式嗎，原來長甚麼樣子
    return features
#print(document_features(documents[0][0]))
#documents怎麼會是二維的，是tuple，所以這裡只是查看，沒有甚麼意思
#'contains(跟)': True

N_testing = 20
#print(datetime.datetime.now())
featuresets = [(document_features(d), c) for (d,c) in documents]    # 15 seconds...
train_set, test_set = featuresets[N_testing:], featuresets[:N_testing]

from nltk import NaiveBayesClassifier
classifier = NaiveBayesClassifier.train(train_set)  
#print(datetime.datetime.now()) 
from nltk import classify
print(classify.accuracy(classifier, test_set)) #1.0

print(classifier.show_most_informative_features(5))

# What are the most informative training features in your PTT text prediction task? 
# do they make sense to you?

