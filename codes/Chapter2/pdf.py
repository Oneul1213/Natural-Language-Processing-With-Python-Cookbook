# 2장 처리 전 텍스트 소싱 및 정규화 - 파이썬에서 PDF 파일 읽기
from PyPDF2 import PdfFileReader


# PDF 파일 읽기 함수 정의
def getTextPDF(pdfFileName, password=''):
    pdf_file = open(pdfFileName, 'rb')   # 파일 열기
    read_pdf = PdfFileReader(pdf_file)   # 열린 파일을 PdfFileRader로 전달

    if password != '':
        read_pdf.decrypt(password)   # 암호 해제

    text = []
    for i in range(0, read_pdf.getNumPages()-1):
        text.append(read_pdf.getPage(i).extractText())   # 각 페이지의 텍스트를 문자열 리스트에 추가

    return '\n'.join(text)
