# TF-IDF
TFIDF is a statistical measure that reflects how important a word is to a document.

TF-IDF stands for “Term Frequency — Inverse Data Frequency” \
**Term Frequency (tf)**: gives us the frequency of the word in each document in the corpus. 
```
def term_frequency(term, tokenized_document):
    return tokenized_document.count(term)
```

In this project author has used augmented_term_frequency.

```
def augmented_term_frequency(term, tokenized_document):
    max_count = max([term_frequency(t, tokenized_document) for t in tokenized_document])
    return (0.5 + ((0.5 * term_frequency(term, tokenized_document))/max_count))
```

● Augmented_term_frequency is a way to normalize the document. If we'll not apply normalization then the algorithm will be biased towards longer documents. 

```
def inverse_document_frequencies(tokenized_documents):
     idf_values[tkn] = 1 + math.log(len(tokenized_documents)/(sum(contains_token)))
    return idf_values
```

len(tokenized_documents) = Number of Documents \
sum(contains_token) =  Number of documetns containing the tkn.

● **Inverse Data Frequency (idf)**: used to calculate the weight of rare words across all documents in the corpus. The words that occur rarely in the corpus have a high IDF score\
tfidf final score = TFxIDF

### Applications of TFIDF:
1. Information Retrieval
2. Text mining
3. User Modeling
4. Keyword Extraction
5. Search Engine
6. Computing similarity between text.

## About Project

The project is about designing and implementing TF-IDF. \
In this project the author has designed- \
● APIs that accepts a set of documents and stores them. \
● APIs that accepts a string, performs and display similarity score of the input with the documents \
● Test cases for both endpoints and Tf-IDF functions. \
****Author has followed pep8 (https://www.python.org/dev/peps/pep-0008/) convention in this project.**

## Testing
1. In this project unittest library has been used for testing. 
2. Overall 11 testcases has been written. (We can add more testcases but as of now author has made 11 cases)
3. To run the test cases:- \
  3.1 From cmd line go to slang_labs_backend folder(No need to run the server) \
  3.2 from cmd line run = python -m unittest discover 
4. Test cases has been divided into 2 classes/groups:- \
  4.1 Endpoint testing \
  4.2 Function (tf-idf) testing 

## How to Install and Run the server

1. From cmd line go to slang_labs_backend folder
2. Install pipenv For example : for windows = pip install --user pipenv,and add to your PATH (https://github.com/pypa/pipenv)
3. Commands to execute \
  3.1 pipenv shell \
  3.2 pipenv install 
4. To run the server = python app.py

## How to navigate client side
1. Go to slang_labs_client
2. There will be two files and  : \
  2.1 Upload.py - You can upload multiple .TXT files using this python script. \
  2.2 text_input.py - You can get similarity score of your input with the uploaded file. 
3. When runing the code for 1st time, first follow 2.1 then run 2.2 <br>
****Run the server(python app.py) before runing the clinet side code.**

## Dependencies 
1. Python - 3.8
2. pipenv
