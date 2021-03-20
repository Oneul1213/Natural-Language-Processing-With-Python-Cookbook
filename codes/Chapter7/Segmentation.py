# 7장 정보 추출과 텍스트 분류 - 분류기를 사용한 문장 분할
import nltk


def featureExtractor(words, i):
    return({'current-word': words[i], 'next-is-upper':
           words[i+1][0].isupper()}, words[i+1][0].isupper())


def getFeaturesets(sentence):
    words = nltk.word_tokenize(sentence)
    featuresets = [featureExtractor(words, i) for i in range(1, len(words)-1)
                   if words[i] == '.']
    return featuresets


def segmentTextAndPrintSentences(data):
    words = nltk.word_tokenize(data)
    for i in range(0, len(words) - 1):
        if words[i] == '.':
            if classifier.classify(featureExtractor(words, i)[0]):
                print(".")
            else:
                print(words[i], end='')
        else:
            print("{} ".format(words[i]), end='')
    print(words[-1])


traindata = "India, officially the Republic of India, is a country in South Asia. It is the second-most populous country, the seventh-largest country by land area, and the most populous democracy in the world. Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west; China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand and Indonesia."
testdata = "Modern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago. Their long occupation, initially in varying forms of isolation as hunter-gatherers, has made the region highly diverse, second only to Africa in human genetic diversity. Settled life emerged on the subcontinent in the western margins of the Indus river basin 9,000 years ago, evolving gradually into the Indus Valley Civilisation of the third millennium BCE. By 1200 BCE, an archaic form of Sanskrit, an Indo-European language, had diffused into India from the northwest, unfolding as the language of the Rigveda, and recording the dawning of Hinduism in India. The Dravidian languages of India were supplanted in the northern and western regions. By 400 BCE, stratification and exclusion by caste had emerged within Hinduism, and Buddhism and Jainism had arisen, proclaiming social orders unlinked to heredity. Early political consolidations gave rise to the loose-knit Maurya and Gupta Empires based in the Ganges Basin. Their collective era was suffused with wide-ranging creativity, but also marked by the declining status of women, and the incorporation of untouchability into an organised system of belief. In South India, the Middle kingdoms exported Dravidian-languages scripts and religious cultures to the kingdoms of Southeast Asia."

traindataset = getFeaturesets(traindata)
classifier = nltk.NaiveBayesClassifier.train(traindataset)
segmentTextAndPrintSentences(testdata)
