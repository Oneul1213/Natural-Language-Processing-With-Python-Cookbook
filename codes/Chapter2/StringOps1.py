# 2장 처리 전 텍스트 소싱, 정규화 - 문자열 연산의 중요성
# 객체 정의
namesList = ['유나', '지은', '스튜어트', '케빈']
sentence = '우리 강아지는 소파 위에서 잔다'

# join
names = ';'.join(namesList)
print(type(names), ':', names)

# split
wordList = sentence.split(' ')
print((type(wordList)), ':', wordList)

# +와 *의 사용
additionExample = '파이썬' + '파이썬' + '파이썬'
multiplicationExample = '파이썬' * 2
print('텍스트 덧셈 :', additionExample)
print('텍스트 곱셈 :', multiplicationExample)

# 문자열 인덱스
str = 'Python NLTK'
print(str[1])
print(str[-3])
