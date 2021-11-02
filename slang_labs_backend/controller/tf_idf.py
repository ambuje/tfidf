from controller.utils import savenmpy, savenmpy_file
from controller.pre_process import preprocess
import math
import os


def term_frequency(term, tokenized_document):
    return tokenized_document.count(term)


def augmented_term_frequency(term, tokenized_document):
    max_count = max([term_frequency(t, tokenized_document)
                    for t in tokenized_document])
    return (0.5 + ((0.5 * term_frequency(term,
                    tokenized_document)) / max_count))


def inverse_document_frequencies(tokenized_documents):

    idf_values = {}
    all_tokens_set = set(
        [item for sublist in tokenized_documents for item in sublist])
    # print(all_tokens_set)
    for tkn in all_tokens_set:
        contains_token = map(lambda doc: tkn in doc, tokenized_documents)
        idf_values[tkn] = 1 + \
            math.log(len(tokenized_documents) / (sum(contains_token)))
    return idf_values


def tfidf(documents):

    for i in documents:
        if i == "" or i == ' ':
            return None

    preprocessed_documents = preprocess(documents)
    # print(preprocessed_documents)
    idf = inverse_document_frequencies(preprocessed_documents)
    # print(idf)
    tfidf_documents = []
    for document in preprocessed_documents:
        tff = []
        doc_tfidf = []
        for term in idf.keys():
            tf = augmented_term_frequency(term, document)
            tff.append(tf)
            doc_tfidf.append(tf * idf[term])
        # print(tff)
        tfidf_documents.append(doc_tfidf)
    return tfidf_documents


def cosine_similarity(vector1, vector2):
    dot_product = sum(p * q for p, q in zip(vector1, vector2))
    magnitude = math.sqrt(sum([val**2 for val in vector1])) * \
        math.sqrt(sum([val**2 for val in vector2]))
    if not magnitude:
        return 0
    return dot_product / magnitude


def read_doc():

    all_docu = []
    arr = os.listdir('./uploads')
    # print(arr)
    for file in arr:
        with open("./uploads/" + file) as f:
            lines = f.readlines()
            all_docu.extend(lines)

    tfidf_documents = tfidf(all_docu)
    savenmpy(tfidf_documents)
    savenmpy_file(arr)
