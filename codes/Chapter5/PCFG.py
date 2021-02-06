# 5장 품사 태깅과 문법 - 확률적 문맥 무관 문법-CFG 작성
import nltk
from nltk.parse.generate import generate

# 시작 심볼 : ROOT
# 비터미널 : WORD, P1, P2, P3, P4
# 터미널 : 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
productions = [
    "ROOT -> WORD [1.0]",            # WORD 심볼의 확률은 1.0
    "WORD -> P1 [0.25]",             # WORD 심볼은 0.25의 확률로 P1을 생성한다
    "WORD -> P1 P2 [0.25]",          # ...
    "WORD -> P1 P2 P3 [0.25]",
    "WORD -> P1 P2 P3 P4 [0.25]",
    "P1 -> 'A' [1.0]",
    "P2 -> 'B' [0.5]",
    "P2 -> 'C' [0.5]",
    "P3 -> 'D' [0.3]",
    "P3 -> 'E' [0.3]",
    "P3 -> 'F' [0.4]",
    "P4 -> 'G' [0.9]",
    "P4 -> 'H' [0.1]",
]

grammarString = "\n".join(productions)

grammar = nltk.PCFG.fromstring(grammarString)

print(grammar)

for sentence in generate(grammar, n=10, depth=5):
    palindrome = "".join(sentence).replace(" ", "")
    print("String : {}, Size : {}".format(palindrome, len(palindrome)))
