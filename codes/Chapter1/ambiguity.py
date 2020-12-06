# 1장 말뭉치와 워드넷 - 모호한 단어를 가지고 워드넷을 사용해 모든 의미 탐구
from nltk.corpus import wordnet as wn
chair = 'chair'

# 의자(chair)의 동의어 집합(Synset) 호출 및 출력
chair_synsets = wn.synsets(chair)
print('의자(Chair)의 뜻 Synsets :', chair_synsets, '\n\n')

# Synset 리스트의 의미별 정의, 기본형/동의어, 문장에서의 예 출력
for synset in chair_synsets:
    print(synset, ': ')
    print('Definition: ', synset.definition())
    print('Lemmas/Synonymous words: ', synset.lemma_names())
    print('Example: ', synset.examples(), '\n')
