#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence is None:
        return(0, None)
    else:
        return(length, sentence[0])
