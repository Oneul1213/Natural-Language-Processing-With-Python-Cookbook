# 3장 전처리 - 편집거리-두 문자열 간의 편집 거리를 찾기 위한 알고리즘 작성
from nltk.metrics.distance import edit_distance


# 편집 거리 계산 함수
def my_edit_distance(str1, str2):
    m = len(str1)+1
    n = len(str2)+1
    
    table = {}
    for i in range(m):
        table[i, 0] = i