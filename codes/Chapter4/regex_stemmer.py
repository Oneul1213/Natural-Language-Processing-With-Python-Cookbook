# 4장 정규표현식 - 자체 정규식 스테머 사용법
import re


# 스테밍 함수 선언
def stem(word):
    # 있거나 없는(?) 어간과 있거나 없는 접미사의 두 그룹으롭 분할
    splits = re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$', word)
    stem = splits[0][0]
    return stem


# 입력 문장
raw = "Keep your friends close, but your enemies closer."

# 토큰화
tokens = re.findall(r'\w+|\S\w*', raw)
print(tokens)

# 스테밍
for t in tokens:
    print("'"+stem(t)+"'")
