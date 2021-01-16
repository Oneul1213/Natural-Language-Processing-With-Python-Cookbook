# 4장 정규표현식 - 정규표현식-*, +, ? 사용법
import re


def text_match(text, patterns):
    if re.search(patterns, text):
        return('일치하는 항목을 찾았습니다!')
    else:
        return('일치하지 않음!')


# b? : b가 0개 또는 1개
print(text_match("ac", "ab?"))
print(text_match("abc", "ab?"))
print(text_match("abbc", "ab?"))

# b* : b가 0개 이상
print(text_match("ac", "ab*"))
print(text_match("abc", "ab*"))
print(text_match("abbc", "ab*"))

# b+ : b가 1개 이상
print(text_match("ac", "ab+"))
print(text_match("abc", "ab+"))
print(text_match("abbc", "ab+"))

# b{2} : b가 2개
print(text_match("abbc", "ab{2}"))

# b{3,5} : b가 3개 이상 5개 이하
print(text_match("aabbbbc", "ab{3,5}"))
