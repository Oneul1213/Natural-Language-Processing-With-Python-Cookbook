# 8장 고급 NLP 레시피 - 텍스트 유사도 문제 해결
import nltk
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TextSimilarityExample:
    def __init__(self):            # 샘플 문장 생성
        self.statements = [
            'ruled india',
            'Chalukyas ruled Badami',
            'So many kingdoms ruled India',
            'Lalbagh is a botanical garden in India'
        ]
    
    def TF(self, sentence):        # 문서 내 모든 단어의 TF(용어 빈도)
        words = nltk.word_tokenize(sentence.lower())
        freq = nltk.FreqDist(words)
        dictionary = {}
        for key in freq.keys():
            norm = freq[key]/float(len(words))
            dictionary[key] = norm            # 단어의 빈도 분포를 부동 소수점 값으로 저장
        return dictionary
    
    def IDF(self):                # 문서 내 모든 단어의 IDF(역 문서 빈도) 값을 찾음 
        def idf(TotalNumberOfDocuments, NumberOfDocumentsWithThisWord):
            return 1.0+math.log(TotalNumberOfDocuments/NumberOfDocumentsWithThisWord)    # IDF를 찾는 공식
        numDocuments = len(self.statements)
        uniqueWords = {}
        idfValues = {}
        for sentence in self.statements:        # 모든 문서에 있는 각 단어 개수 확인
            for word in nltk.word_tokenize(sentence.lower()):
                if word not in uniqueWords:
                    uniqueWords[word] = 1
                else:
                    uniqueWords[word] += 1
        for word in uniqueWords:
            idfValues[word] = idf(numDocuments, uniqueWords[word])    # 모든 단어에 대한 IDF 값 구해서 저장
        return idfValues
    
    def TF_IDF(self, query):
        words = nltk.word_tokenize(query.lower())
        idf = self.IDF()
        vectors = {}
        for sentence in self.statements:
            tf = self.TF(sentence)
            for word in words:
                tfv = tf[word] if word in tf else 0.0
                idfv = idf[word] if word in idf else 0.0
                mul = tfv * idfv            # 모든 문장의 모든 단어에 대한 TF, IDF 값을 찾아 TF_IDF(TF * IDF)를 구함
                if word not in vectors:
                    vectors[word] = []
                vectors[word].append(mul)
        return vectors
    
    def displayVectors(self, vectors):        # 벡터 출력
        print(self.statements)
        for word in vectors:
            print("{} -> {}".format(word, vectors[word]))
    
    def cosineSimilarity(self):        # 코사인 유사도 계산(scikit 이용)
        vec = TfidfVectorizer()
        matrix = vec.fit_transform(self.statements)        # 행렬 작성
        for j in range(1, 5):
            i = j - 1
            print("\tsimilarity of document {} with others".format(i))
            similarity = cosine_similarity(matrix[i:j], matrix)
            print(similarity)
    
    def demo(self):
        inputQuery = self.statements[0]
        vectors = self.TF_IDF(inputQuery)
        self.displayVectors(vectors)
        self.cosineSimilarity()

similarity = TextSimilarityExample()
similarity.demo()
