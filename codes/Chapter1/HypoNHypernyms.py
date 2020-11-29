# 1장 말뭉치와 워드넷 - 두 개의 구별되는 동의어 집합을 선택하고 워드넷을 사용해 상위어와 하위어 개념 탐색
# 라이브러리 import 및 synset 초기화
from nltk.corpus import wordnet as wn
woman = wn.synset('woman.n.01')
bed = wn.synset('bed.n.01')

# 동의어 집합 출력, 루트 노드에서 synset까지의 경로를 포함하는 집합의 리스트 얻기
print(woman.hypernyms())
woman_paths = woman.hypernym_paths()

# root에서부터의 경로 출력
for idx, path in enumerate(woman_paths):
    print('\n\n상위어 경로 :', idx + 1)
    for synset in path:
        print(synset.name(), ', ', end='')
print()

# bed의 하위어 출력
types_of_beds = bed.hyponyms()
print('\n\nbed의 형태(하위어): ', types_of_beds)

# 기본형(lemmas) 출력
print(sorted(set(lemma.name() for synset in types_of_beds for lemma in synset.lemmas())))
