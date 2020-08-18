#!/bin/bash
#takes in a URL, POST request to the passed URL & displays body of response
curl -s "$1" -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
