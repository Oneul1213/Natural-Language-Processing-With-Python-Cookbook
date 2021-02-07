#  6장 청킹, 문자아 구문 분석, 의존성 - 내장 청커 사용
import nltk


text = "Lalbagh Botanical Gardens is a well known botanical garden in Bengaluru, India."
sentences = nltk.sent_tokenize(text)

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    chunks = nltk.ne_chunk(tags)
    print(chunks)
