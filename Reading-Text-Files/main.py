# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from cgitb import text
from typing import Dict


def read_file_content(filename): 
    # [assignment] Add your code here 
    with open(filename, 'r') as read_file:
        return read_file.read()


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = text.split()
    text_dict = dict()
    for word in text:
        #didn't use if -elif statements incase two symbols appear in a word
        if '?' in word:
            word = word.replace('?','')
        if '.' in word:
            word = word.replace('.','')
        if ',' in word:
            word = word.replace(',','')
        #adding keys and values to the text_dict dictionary
        if word in text_dict:
            text_dict[word] += 1
        else:
            text_dict[word] = 1
    return text_dict