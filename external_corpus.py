#1장 말뭉치와 워드넷 - 외부 말뭉치 다운로드, 로드하고 액세스하기
from nltk.corpus import CategorizedPlaintextCorpusReader
from random import randint

# 말뭉치 읽기
reader = CategorizedPlaintextCorpusReader(r'/workspace/Python/NLP/mix20_rand700_tokens_cleaned/tokens', r'.*\.txt', cat_pattern=r'(\w+)/*')
print(reader.categories())
print(reader.fileids())

# 샘플 문서 출력
# pos, neg 카테고리의 샘플 목록
posFiles = reader.fileids(categories='pos')
negFiles = reader.fileids(categories='neg')

# pos, neg 카테고리에서 각각 임의의 파일 선택
fileP = posFiles[randint(0, len(posFiles)-1)]
fileN = negFiles[randint(0, len(negFiles)-1)]
print(fileP)
print(fileN)

# 액세스한 임의 파일을 문장으로 출력
for w in reader.words(fileP):
    print(w + ' ', end='')
    if w is '.':
        print()
for w in reader.words(fileN):
    print(w + ' ', end='')
    if w is '.':
        print()