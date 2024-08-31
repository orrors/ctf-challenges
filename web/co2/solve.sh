#!/bin/bash

curl 'http://localhost:1337/register' -X POST -d 'username=a&password=a'
curl 'http://localhost:1337/login' -X POST -d 'username=a&password=a' --cookie-jar /tmp/cookie-jar
curl 

