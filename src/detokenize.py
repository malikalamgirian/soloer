import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer


# De-tokenize using NLTK
def detokenize(list_to_detokenize):
    sentence = TreebankWordDetokenizer().detokenize(list_to_detokenize)
    print("\nNLTK Sentential form: " + sentence + "\n")
    return sentence
