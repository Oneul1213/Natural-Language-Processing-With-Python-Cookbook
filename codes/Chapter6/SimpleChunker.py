# 6장 청킹, 문장 구문 분석, 의존성 - 간단한 청커 작성법
import nltk


text = "Ravi is the CEO of a Company. He is very powerful public speaker also."

# 품사를 사용해 작성된 정규식(태그 패턴)
grammar = '\n'.join([
    'NP: {<DT>*<NNP>}',
    'NP: {<JJ>*<NN>}',
    'NP: {<NNP>+}',
])

sentences = nltk.sent_tokenize(text)

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    chunkparser = nltk.RegexpParser(grammar)
    result = chunkparser.parse(tags)
    print(result)
