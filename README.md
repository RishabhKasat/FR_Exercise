# FR_Exercise

## Requirement 
- Python3.5 or later version

## How to run the file
- Download the FR.py file
- Double click to run the file
- The code will ask to input the first sentences for comparison. Type in the sentence and hit enter
- The code will further ask to input the second sentence. Type in the second sentence and hit enter

## Result
- The output is a numeric value with range between 0 and 1. 0 = No similarity , 1 = Exact Match

## Methodology

In the above code has three functions:
- remove_stop_words
- countvec 
- cosine

*remove_stop_words* takes the text(sentence) as the input and returns a list of words after removes all the stopwords and special characters from the code

*countvec* it takes two a list and a set. Set contains all the unique words from both the sentences. list contains the words from a single input sentence. The function generates a dictionary which contains the unique words from both the sentence as the key and vales as the count of the specific word in the list. The function returns a list which contains the count of each of the key(word) in a dictionary

*cosine* it takes input the lists returned from countvec and computes the cosine similarity between them.


## Areas of improvement

The code can be improved by using more comprehensive approach.If use of libraries were permited. I would have lemmatized the word to bring them to their root form and used algorithms like Latent Semantic Indexing or Latent Dirichlet Allocation to have a better algorithm for predicting similarity between sentences. Furthermore, Neural Networs can also be used .
