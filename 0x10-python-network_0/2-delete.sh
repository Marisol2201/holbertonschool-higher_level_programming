#!/bin/bash
#DELETE request to URL passed as the 1th arg & displays the body of response
curl -sX DELETE "$1"
