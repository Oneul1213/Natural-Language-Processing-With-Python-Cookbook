# 7장 정보 추출과 텍스트 분류 - 내장 개체명 인식 기능 사용
import nltk


def sampleNE():
    sent = nltk.corpus.treebank.tagged_sents()[0]
    print(nltk.ne_chunk(sent))

def sampleNE2():
    sent = nltk.corpus.treebank.tagged_sents()[0]
    print(nltk.ne_chunk(sent, binary=True))


if __name__ == '__main__':
    sampleNE()
    sampleNE2()
