#!/bin/bash
#takes in a URL as arg, GET request to the URL & displays body of response
curl -s "$1" -H "X-HolbertonSchool-User-Id:98"
