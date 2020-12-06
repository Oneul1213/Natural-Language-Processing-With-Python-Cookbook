# 1장 말뭉치와 워드넷 - 브라운 코퍼스에서 세 가지 장르의 wh 단어 모두 세기
import nltk
from nltk.corpus import brown

# 말뭉치의 모든 장르 리스트 출력
print(brown.categories())

# 장르와 whwords 선택
genres = ['fiction', 'humor', 'romance']
whwords = ['what', 'which', 'how', 'why', 'when', 'where', 'who']

# FreqDist를 이용하여 장르 별 wh 단어의 빈도 수 출력
for i in range(0, len(genres)):
    genre = genres[i]
    print()
    print("'" + genre + "' wh 단어 분석")
    genre_text = brown.words(categories=genre)

    fdist = nltk.FreqDist(genre_text)

    for wh in whwords:
        print(wh + ':', fdist[wh], end=' ')
print()
