# 2장 처리 전 텍스트, 소싱, 정규화 - 파이썬에서 워드 문서 읽기
# python-docx의 docx 객체
import docx


def getTextWord(wordFileName):
    doc = docx.Document(wordFileName)   # doc 객체에 읽을 word 파일 로드

    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)    # 단락별로 문서 읽고 fullText에 추가

    return '\n'.join(fullText)
