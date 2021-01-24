# 4장 정규표현식 - 자체 정규식 토크나이저 작성법
import re


raw = "I am big! It's the pictures that got small."
# 하나 이상의 공백으로 자르기
print(re.split(r' +', raw))
# 하나 이상의 단어가 아닌 문자로 나누기
print(re.split(r'\W+', raw))
# 하나 이상의 단어, 또는 공백(\s, space)이 아닌 단어(\S)와 0개 이상의 단어 모두 찾기
print(re.findall(r'\w+|\S\w*', raw))
