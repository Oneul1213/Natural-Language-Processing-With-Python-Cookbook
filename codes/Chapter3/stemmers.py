# 3장 전처리 - 스테밍-NLTK 내장 스테머 사용법
from nltk import PorterStemmer, LancasterStemmer, word_tokenize


# 입력 텍스트 토큰화
raw = "My name is Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions and loyal servant to the true emperor, Marcus Aurlius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next."
tokens = word_tokenize(raw)

# 포터 스테머(PorterStemmer)
porter = PorterStemmer()
pStems = [porter.stem(t) for t in tokens]
print(pStems)

# 랭커스터 스테머(LancasterStemmer)
lancaster = LancasterStemmer()
lStems = [lancaster.stem(t) for t in tokens]
print(lStems)
