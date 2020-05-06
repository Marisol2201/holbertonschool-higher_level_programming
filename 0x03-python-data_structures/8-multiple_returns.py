#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if (sentence is None) or (length is None):
            return
    for letter in sentence:
        return(length, letter)
