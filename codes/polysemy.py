# 1장 말뭉치와 워드넷 - 워드넷으로 명사, 동사, 형용사, 부사의 다의어 평균 계산
# 라이브러리 import 및 품사 유형 초기화(n : 명사, v : 동사, r : 부사, a : 형용사)
from nltk.corpus import wordnet as wn
type = 'n'
# type = 'v'
# type = 'r'
# type = 'a'

# 워드넷 데이터베이스에 존재하는 명사 유형 n의 모든 synset을 반환
synsets = wn.all_synsets(type)

# 기본형(lemma) 리스트 초기화
# lemmas = []
# for synset in synsets:
#     for lemma in synset.lemmas():
#         lemmas.append(lemma.name())

# pythonic version
lemmas = [lemma.name() for synset in synsets for lemma in synset.lemmas()]

# 중복 제거
lemmas = set(lemmas)

# 각 lemma의 뜻 세기(count)
count = 0
for lemma in lemmas:
    count = count + len(wn.synsets(lemma, type))

# 출력
print('개별 기본형 합계: ', len(lemmas))
print('총 뜻: ', count)
print(type, '(명사)의 다의어 평균: ', count/len(lemmas))
