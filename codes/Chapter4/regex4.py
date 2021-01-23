# 4장 정규표현식 - 날짜 정규표현식과 문자 집합 또는 문자 범위 집합 만들기
import re


# 문자열 객체 선언
url = "http://www.telegraph.co.uk/formula-1/2018/10/28/mexican-grand-prix-2017-time-does-start-tv-channel-odds-lewis1/"
date_regex = '/(\d{4})/(\d{1,2})/(\d{1,2})/'

# url에서 date_regex 찾기
print("URL에서 찾은 날짜 :", re.findall(date_regex, url))

# 패턴 집합 확인 함수
def is_allowed_specific_char(string):
    # r(raw string) : 백슬래시를 일반 문자로 취급(백슬래시를 두 번 안써도 되도록 함)
    charRe = re.compile(r'[^a-zA-z0-9.]')    # a-z, A-Z, 0-9, . 범위의 문자가 아님(^) 이라는 패턴 생성
    string = charRe.search(string)    # 컴파일 된 패턴을 string에서 찾음
    return not bool(string)

# 패턴 테스트
print(is_allowed_specific_char("ABCDEFabcdef123450."))
print(is_allowed_specific_char("*&%@#!}{"))
