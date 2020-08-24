#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header"""
import requests
import sys


if __name__ == "__main__":
    """Your code should not be executed when imported"""
    url = sys.argv[1]
    ans = requests.get(url)
    print(ans.headers.get("X-Request-Id"))
