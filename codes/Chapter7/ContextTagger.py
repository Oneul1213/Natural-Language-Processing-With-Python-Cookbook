# 7장 정보 추출과 텍스트 분류 - 문맥 기반 품사 태거 작성
import nltk
sentences = [
    "What is your address when you're in Bangalore?",
    "the president's address on the state of the economy.",
    "He addressed his remarks to the lawyers in the audience.",
    "In order to address an assembly, we should be ready.",
    "He laughed inwardly at the scene.",
    "After all the advance publicity, the prizefight turned out to be a laugh.",
    "We can learn to laugh a little at even our most serious foibles."
]


def getSentenceWords():
    sentwords = []
    for sentence in sentences:
        words = nltk.pos_tag(nltk.word_tokenize(sentence))
        sentwords.append(words)
    return sentwords


def noContextTagger():
    tagger = nltk.UnigramTagger(getSentenceWords())
    print(tagger.tag('the little remarks towards assembly are laughable'
                     .split()))


def withContextTagger():
    def wordFeatures(words, wordPosInSentence):
        # 모든 ing 형태 등을 추출
        endFeatures = {
            'last(1)': words[wordPosInSentence][-1],
            'last(2)': words[wordPosInSentence][-2:],
            'last(3)': words[wordPosInSentence][-3:],
        }
        # 이전 단어를 사용해 현재 단어가 동사인지 명사인지 확인
        if wordPosInSentence > 1:
            endFeatures['prev'] = words[wordPosInSentence - 1]
        else:
            endFeatures['prev'] = '|NONE|'
        return endFeatures
    allsentences = getSentenceWords()
    featureddata = []
    for sentence in allsentences:
        untaggedSentence = nltk.tag.untag(sentence)
        featuredsentence = [(wordFeatures(untaggedSentence, index), tag)
                            for index, (word, tag) in enumerate(sentence)]
        featureddata.extend(featuredsentence)
    breakup = int(len(featureddata) * 0.5)
    traindata = featureddata[breakup:]
    testdata = featureddata[:breakup]
    classifier = nltk.NaiveBayesClassifier.train(traindata)
    print("Accuracy of the classifier : {}"
          .format(nltk.classify.accuracy(classifier, testdata)))


noContextTagger()
withContextTagger()
