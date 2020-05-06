#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
            return
    for letter in sentence:
        return(len(sentence), letter)
