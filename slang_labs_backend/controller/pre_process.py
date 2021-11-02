import re
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')


def preprocess(all_document):
    ps = PorterStemmer()
    def tokenize(doc): return doc.lower().split(" ")

    def punctuation(document):
        # print(document)
        symbols = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
        for i in symbols:
            if i in document:
                document = document.replace(i, "")
#        print('data', document)
        return document

    def stopwords(document):
        # print(document)
        from nltk.corpus import stopwords
        pattern = re.compile(
            r'\b(' + r'|'.join(stopwords.words('english')) + r')\b\s*')
        text = pattern.sub('', str(document)).strip()
        return text

    def stemm(document):

        text1 = ''
        words = word_tokenize(document)
        # print(words)
        for w in words:
            stm = ps.stem(w)
            text1 = text1 + stm + ' '
        # print(text1)
        text1 = text1.strip()
        return text1

    preproc_list = []
    for i in range(0, len(all_document)):
        raw_text = all_document[i]
        raw_txt = punctuation(raw_text)

        raw_txt = stopwords(raw_txt)
        raw_txt = stemm(raw_txt)
        raw_txt = punctuation(raw_txt)
        # print(raw_txt)

        preproc_list.append(raw_txt)
    # print("list",l)
    tokenized_txt = [tokenize(d) for d in preproc_list]
    return tokenized_txt
