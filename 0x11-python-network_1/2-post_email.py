#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response"""
from sys import argv
from urllib import parse, request


if __name__ == "__main__":
    """Your code should not be executed when imported"""
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email})
    req = request.Request(url, data.encode('utf-8'))
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
