import numpy as np


def savenmpy(final_tfidf):
    # print('np')

    np.save('./tfidfvectors/tfidf.npy', final_tfidf)


def savenmpy_file(arr):
    # print('np')

    np.save('./tfidfvectors/file_name.npy', arr)


def loadnp():
    a = np.load('./tfidfvectors/tfidf.npy')
    return a


def loadnp_file():
    a = np.load('./tfidfvectors/file_name.npy')
    return a
