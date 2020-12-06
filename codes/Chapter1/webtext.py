# 1장 말뭉치와 워드넷 - 웹 및 채팅 텍스트 자료 파일 중 하나에서 빈도 분포 작업 탐색
import nltk, matplotlib
from nltk.corpus import webtext

# webtext를 구성하는 파일 명 출력
print(webtext.fileids())

# 'sigles.txt' 파일의 단어들의 빈도 구하기
fileid = 'singles.txt'
wbt_words = webtext.words(fileid)
fdist = nltk.FreqDist(wbt_words)

# 가장 일반적으로 나타나는 단어와 해당 단어의 개수 출력
print('최대 발생 토큰  "', fdist.max(), '" 수 : ', fdist[fdist.max()])

# 말뭉치 내의 단어 수
print('말뭉치 내 총 고유 토큰 수 : ', fdist.N())

# 말뭉치에서 가장 빈번한 단어 10개 출력
print('말뭉치에서 가장 흔한 10개 단어는 다음과 같습니다.')
print(fdist.most_common(10))

# 모든 단어의 빈도 분포 표 출력
print('개인 광고의 빈도 분포')
print(fdist.tabulate())

# 누적 빈도 도수 분포 그래프 출력
fdist.plot(cumulative=True)
