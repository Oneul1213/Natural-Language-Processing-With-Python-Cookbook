# 2장 처리 전 텍스트, 소싱, 정규화
from bs4 import BeautifulSoup


# HTML파일을 BeautifulSoup 객체로 로드
html_doc = open('Files/sample-html.html', 'r').read()
soup = BeautifulSoup(html_doc, 'html.parser')

# HTML 태그 제거
print('\n\nHTML이 제거된 전체 텍스트 :')
print(soup.get_text())

# title 태그 가져오기
print('<title> 태그에 액세스 :', end=' ')
print(soup.title)

# h1 태그에서 태그 제거 후 가져오기
print('<H1> 태그의 텍스트에 액세스 :', end=' ')
print(soup.h1.string)

# img 태그의 alt 속성 가져오기
print('<img> 태그의 속성에 액세스 :', end=' ')
print(soup.img['alt'])

# 특정 태그 모두 가져오기
print('\n 존재하는 모든 <p> 태그에 액세스 :')
for p in soup.find_all('p'):
    print(p.string)
