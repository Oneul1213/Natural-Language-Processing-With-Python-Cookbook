# 5장 품사 태깅과 문법 - 재귀 CFG 작성
import nltk
import string
from nltk.parse.generate import generate

productions = [
    "ROOT -> WORD",
    "WORD -> ' '"
]

alphabets = list(string.digits)

for alphabet in alphabets:
    productions.append("WORD -> '{w}' WORD '{w}'".format(w=alphabet))

grammarString = "\n".join(productions)

grammar = nltk.CFG.fromstring(grammarString)

print(grammar)

for sentence in generate(grammar, n=5, depth=5):
    palindrome = "".join(sentence).replace(" ", "")
    print("Palindrome : {}, Size : {}".format(palindrome, len(palindrome)))
