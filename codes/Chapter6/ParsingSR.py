# 6장 청킹, 문장 구문 분석, 의존성 - 시프트 변환 구문 분석
import nltk


def SRParserExample(grammar, textlist):
    parser = nltk.parse.ShiftReduceParser(grammar)
    for text in textlist:
        sentence = nltk.word_tokenize(text)
        for tree in parser.parse(sentence):
            print(tree)
            # tree.draw()    # 구름 ide에서 실행 안됨


text = [
    "Tajmahal is in Agra",
    "Bangalore is the capital of Karnataka",
]

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> NNP VBZ
VP -> IN NNP | DT NN IN NNP
NNP -> 'Tajmahal' | 'Agra' | 'Bangalore' | 'Karnataka'
VBZ -> 'is'
IN -> 'in' | 'of'
DT -> 'the'
NN -> 'capital'
""")

SRParserExample(grammar, text)
