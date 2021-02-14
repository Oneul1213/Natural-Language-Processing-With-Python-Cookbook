# 6장 청킹, 문장 구문 분석, 의존성 - 청커 학습
import nltk
from nltk.corpus import conll2000
from nltk.corpus import treebank_chunk


def mySimpleChunker():
    grammar = 'NP: {<NNP>+}'
    return nltk.RegexpParser(grammar)


def test_nothing(data):
    cp = nltk.RegexpParser("")
    print(cp.evaluate(data))


def test_mysimplechunker(data):
    schunker = mySimpleChunker()
    print(schunker.evaluate(data))


datasets = [
    conll2000.chunked_sents('test.txt', chunk_types=['NP']),
    treebank_chunk.chunked_sents()
]

for dataset in datasets:
    test_nothing(dataset[:50])
    test_mysimplechunker(dataset[:50])
