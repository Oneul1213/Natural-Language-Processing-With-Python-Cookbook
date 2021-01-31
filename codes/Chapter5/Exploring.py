# 5장 품사 태깅과 문법 - 내장 태거 탐구
import nltk
simpleSentence = "Bangalore is the capital of Karnataka."
wordsInsSentence = nltk.word_tokenize(simpleSentence)
print(wordsInsSentence)
partsOfSpeechTags = nltk.pos_tag(wordsInsSentence)
print(partsOfSpeechTags)
