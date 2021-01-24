# 4장 정규표현식 - 문장에서 다섯 글자 단어를 찾고 약어 만들기
import re


# 입력 문자열 정의 및 약어의 대체 패턴 적용
# street에서 Road -> Rd로 변경 후 출력
street = '21 Teheran Road'
print(re.sub('Road', 'Rd', street))

text = 'Diwali is a festival of light, Holi is a festival of color!'
# \b : 빈 문자열, r<pattern> : 원시 문자열 표기법
print(re.findall(r"\b\w{5}\b", text))
