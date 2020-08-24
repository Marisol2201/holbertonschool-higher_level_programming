#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    """Your code should not be executed when imported"""
    url = 'https://intranet.hbtn.io/status'
    ans = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(ans.text)))
    print('\t- content: {}'.format(ans.text))
