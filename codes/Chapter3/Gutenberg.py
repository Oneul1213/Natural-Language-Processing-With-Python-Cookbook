# 3장 전처리 - 불용어-불용어 말뭉치 사용법과 불용어가 만들어내는 차이점 확인
import nltk
from nltk.corpus import gutenberg


# 구텐베르크 텍스트 이름 출력
print(gutenberg.fileids())

# 전처리(bible-kjvc.txt에서 길이가 2자 이하인 단어 삭제)
gb_words = gutenberg.words('bible-kjv.txt')
words_filtered = [e for e in gb_words if len(e) >= 3]

# 불용어 필터링
stopwords = nltk.corpus.stopwords.words('english')
words = [w for w in words_filtered if w.lower() not in stopwords]

# nltk.FreqDist 적용(빈도 분석)
fdistPlain = nltk.FreqDist(words)
fdist = nltk.FreqDist(gb_words)

# 빈도분포 출력
print('Following are the most common 10 words in the bag')
print(fdist.most_common(10))
print('Following are the most common 10 words in the bag minus the stopwords')
print(fdistPlain.most_common(10))
