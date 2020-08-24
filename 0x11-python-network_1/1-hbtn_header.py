#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response"""
import urllib.request
import sys


if __name__ == "__main__":
    """Your code should not be executed when imported"""
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        head = response.headers.get(('X-Request-Id'))
        print(head)
