# 2장 처리 전 텍스트, 소싱, 정규화 - 파이썬에서 PDF 파일 읽기
import pdf

pdfFile = '/workspace/NLP_python/codes/Chapter2/Files/sample-one-line.pdf'
pdfFileEncrypted = '/workspace/NLP_python/codes/Chapter2/Files/sample-one-line.protected.pdf'
print('PDF 1: \n', pdf.getTextPDF(pdfFile))
print('PDF 2: \n', pdf.getTextPDF(pdfFileEncrypted, 'tuffy'))
