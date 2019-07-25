#!/bin/bash

TOKEN=$(curl -d "username=visitor&password=123" -X POST "localhost:8000/api/token/" | python -c "import sys,json; print json.load(sys.stdin)['access']")

curl --location --request GET "localhost:8000/protected" --header "Authorization: Bearer $TOKEN" | jq

curl --location --request GET "localhost:8000/public" | jq
