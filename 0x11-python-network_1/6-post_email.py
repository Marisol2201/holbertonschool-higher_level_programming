#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header"""
import requests
from sys import argv


if __name__ == "__main__":
    """Your code should not be executed when imported"""
    url = argv[1]
    email = argv[2]
    payload = {'email': email}
    r = requests.get(url, params=payload)
    print(r.text)
