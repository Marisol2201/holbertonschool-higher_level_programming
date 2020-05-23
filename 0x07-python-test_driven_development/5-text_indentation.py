#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """function that prints a text with 2 new lines after: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for iter in [".", "?", ":"]:
        if iter in text:
            text = text.replace(iter, iter + '\n\n\a')

    new = text.split('\a')
    for sentence in new:
        print(sentence.strip(' '), end="")
