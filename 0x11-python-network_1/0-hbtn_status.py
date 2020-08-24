#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    """Your code should not be executed when imported"""
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(str(type(body))))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("UTF-8")))
