# 3장 전처리 - 원형 복원-NLTK WordnetLemmatizer 사용법
from nltk import word_tokenize, PorterStemmer, WordNetLemmatizer


# 입력 텍스트 토큰화
raw = "My name is Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions and loyal servant to the true emperor, Marcus Aurlius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next."
tokens = word_tokenize(raw)

# PorterStemmer 적용
porter = PorterStemmer()
stems = [porter.stem(t) for t in tokens]
print(stems)

# lemmatizer 적용
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(t) for t in tokens]
print(lemmas)
