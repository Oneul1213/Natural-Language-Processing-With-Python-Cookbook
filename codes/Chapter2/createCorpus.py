# 2장 처리 전 텍스트, 소싱, 정규화 - PDF, DOCX, 일반 텍스트 파일을 가져와 사용자 정의 말뭉치 생성
import os
import word
import pdf
from nltk.corpus.reader.plaintext import PlaintextCorpusReader


# 일반 텍스트 파일 읽기 함수
def getText(txtFileName):
    file = open(txtFileName, 'r')
    return file.read()


# 말뭉치 폴더 생성
newCorpusDir = 'mycorpus/'
if not os.path.isdir(newCorpusDir):    # 말뭉치 폴더가 이미 존재하는가?
    os.mkdir(newCorpusDir)

# 파일 읽기
# 일반 텍스트 파일
txt1 = getText('./Files/sample_feed.txt')
# PDF 파일
txt2 = pdf.getTextPDF('./Files/sample-pdf.pdf')
# DOCX 파일
txt3 = word.getTextWord('./Files/sample-one-line.docx')

# 파일 쓰기
files = [txt1, txt2, txt3]
for idx, f in enumerate(files):
    with open(newCorpusDir+str(idx)+'.txt', 'w') as fout:
        fout.write(f)

# 사용자 정의 말뭉치 만들기
# 폴더 내의 모든 파일을 읽어와 파일들로부터 말뭉치를 생성한다
newCorpus = PlaintextCorpusReader(newCorpusDir, '.*')

# 사용자 정의 말뭉치가 잘 만들어 졌는지 확인
print(newCorpus.words())    # 말뭉치의 모든 단어를 포함하는 배열
print(newCorpus.sents(newCorpus.fileids()[1]))    # 1.txt에 있는 모든 문장 배열을 출력
print(newCorpus.paras(newCorpus.fileids()[0]))    # 0.txt에 있는 모든 단락 배열을 출력
