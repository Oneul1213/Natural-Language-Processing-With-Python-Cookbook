# 5장 품사 태깅과 문법 - 자체 태거 학습
import nltk
import pickle


def sampleData():
    return [
        "Bangolre is the capital fo Karnataka",
        "Steve Jobs was the CEO of Apple",
        "Books can be purchased in Market",
    ]


def buildDictionary():
    dictionary = {}
    for sent in sampleData():
        parsOfSpeechTags = nltk.pos_tag(nltk.word_tokenize(sent))
        for tag in parsOfSpeechTags:
            value = tag[0]
            pos = tag[1]
            dictionary[value] = pos
    return dictionary


def saveMyTagger(tagger, fileName):
    fileHandle = open(fileName, "wb")
    pickle.dump(tagger, fileHandle)
    fileHandle.close()


def saveMyTraining(FileName):
    tagger = nltk.UnigramTagger(model=buildDictionary())
    saveMyTagger(tagger, fileName)


def loadMyTagger(fileName):
    return pickle.load(open(fileName, "rb"))


sentence = 'Iphone is purchased by Steve Jobs in Bangalore Market'
fileName = "myTagger.pickle"

saveMyTraining(fileName)

myTagger = loadMyTagger(fileName)

print(myTagger.tag(nltk.word_tokenize(sentence)))
