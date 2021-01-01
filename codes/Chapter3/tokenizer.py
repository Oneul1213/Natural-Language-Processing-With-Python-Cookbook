# 3장 전처리 - 토큰화-NLTK 내장 토크나이저 사용법
from nltk.tokenize import LineTokenizer, SpaceTokenizer, TweetTokenizer
from nltk import word_tokenize


# LineTokenizer 사용('줄'로 나누기)
lTokenizer = LineTokenizer();
print("Line toknizer 출력 :", lTokenizer.tokenize("My name is"+
    "Maximus Decimus Meridius, commander of the Armies of the North, "+
    "General of the Felix Legions and loyal servant to the true emperor,"+
    "Marcus Aurlius. \nFather to a murdered son, husband to a murdered"+
    "wife. \nAnd I will have my vengeance, in this life or the next."))

# SpaceTokenizer 사용('공백 문자'로 나누기)
rawText = "By 11 o'clock on sunday, the doctor shall open the dispensary."
sTokenizer = SpaceTokenizer()
print("Space Tokenizer 출력 :", sTokenizer.tokenize(rawText))

# word_tokenize 사용('단어'와 '구두점' 나누기)
print("word Tokenizer 출력 :", word_tokenize(rawText))

# TweetTokenizer 사용('특수문자'를 다룰 때 사용)
tTokenizer = TweetTokenizer()
print("Tweet Tokenizer 출력 :", tTokenizer.tokenize("This is a coooool"+
    "#dummysmiley: :-) :-P <3"))
