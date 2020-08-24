#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body of the
response"""
import urllib.error
from sys import argv
from urllib import parse, request


if __name__ == "__main__":
    """Your code should not be executed when imported"""
    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as err:
        print('Error code: {}'.format(err.code))
