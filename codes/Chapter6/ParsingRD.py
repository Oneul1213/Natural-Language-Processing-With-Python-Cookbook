# 6장 청킹, 문장 구문 분석, 의존성 - 재귀 하향 구문 분석
import nltk


def RDParserExample(grammar, textlist):
    parser = nltk.parse.RecursiveDescentParser(grammar)
    for text in textlist:
        sentence = nltk.word_tokenize(text)
        for tree in parser.parse(sentence):
            print(tree)
            # tree.draw() # 구름 ide에서 python tkinter 프로젝트 필요


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

text = [
    "Tajmahal is in Agra",
    "Bangalore is the capital of Karnataka"
]

RDParserExample(grammar, text)
