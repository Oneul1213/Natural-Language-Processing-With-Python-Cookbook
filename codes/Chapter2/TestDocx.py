# 2장 처리 전 텍스트, 소싱, 정규화 - 파이썬에서 워드 문서 읽기
import docx
import word


# 문서 경로 초기화 및 전체 문서 출력
docName = '/workspace/NLP_python/codes/Chapter2/Files/sample-one-line.docx'
print('Document in full :\n', word.getTextWord(docName))
