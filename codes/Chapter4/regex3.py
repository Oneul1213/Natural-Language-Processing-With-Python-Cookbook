# 4장 정규표현식 - 여러 개의 리터럴 문자열과 하위 문자열 검색
import re


# 패턴과 입력 텍스트 선언 및 정의
patterns = ['Tuffy', 'Pie', 'Loki']
text = 'Tuffy eats pie, Loki eats peas!'

# text에서 pattern 찾기(대소문자 구분)
for pattern in patterns:
    print('"%s"에서 "%s" 검색 중 ->' % (text, pattern))
    if re.search(pattern, text):
        print('찾았습니다!')
    else:
        print('찾을 수 없습니다!')

# 패턴과 입력 텍스트 정의
text = 'Diwali is a festival of lights, Holi is a festival of colors!'
pattern = 'festival'

# text에서 겹치지 않는 모든 pattern을 찾아 이터레이터로 반환
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('%d:%d에서 "%s"을(를) 찾았습니다.' % (s, e, text[s:e]))
