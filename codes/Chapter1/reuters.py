# 1장 말뭉치와 워드넷 - 내부 말뭉치 액세스
from nltk.corpus import reuters

# 파일 목록 및 reuters 말뭉치(corpus)에 있는 각각의 상대 경로 출력
files = reuters.fileids()
print(files)

# 'test/16097 파일의 단어 목록 출력
words16097 = reuters.words(['test/16097'])
print(words16097)

# 16097 파일 단어 중 앞의 20개 출력
words20 = reuters.words(['test/16097'])[:20]
print(words20)

# reuters 말뭉치의 주제(category) 출력
reutersGenres = reuters.categories()
print(reutersGenres)

# bop, cocoa 주제를 문장으로 출력
for w in reuters.words(categories=['bop']):
    print(w+' ', end='')
    if w is '.':
        print()