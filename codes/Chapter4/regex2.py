# 4장 정규표현식 - 정규표현식-$와 ^, 단어의 시작과 끝이 아닌 단어를 사용하는 방법
import re


def text_match(text, patterns):
    if re.search(patterns, text):
        return('일치하는 항목을 찾았습니다!')
    else:
        return('일치하지 않음!')


# . : 줄 바꿈을 제외한 모든 문자와 일치
# a로 시작하고 그 뒤에 0개 이상의 문자가 오고 c로 끝남.
print("테스트 패턴은 다음으로 시작하고 끝남")
print(text_match("abbc", "^a.*c$"))

# \w : 영문, 숫자, 언더바
# 영문, 숫자, 언더바 하나 이상으로 시작
print("단어로 시작함")
print(text_match("Tuffy eats pie, Loki eats peas!", "^\w+"))

# \s : 공백 문자, \S 공백이 아닌 문자(\w 뒤에선 구두점)
# 영문, 숫자, 언더바 하나 뒤에 공백이 아닌 문자 0개 이상으로 끝남
print("단어와 선택적 문장부호로 끝남")
print(text_match("Tuffy eats pie, Loki eats peas!", "\w+\S*$"))

# \b : 단어의 시작이나 끝의 빈 문자열, \B 그 외(단어?)
# 문자 사이에 u가 포함 됨
print("단어의 시작이나 끝이 아닌 문자가 포함된 단어 찾기")
print(text_match("Tuffy eats pie, Loki eats peas!", "\Bu\B"))
