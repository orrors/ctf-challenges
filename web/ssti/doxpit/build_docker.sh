#!/bin/bash
docker rm -f web_dox_pit
docker build -t web_dox_pit . && \
docker run --name=web_dox_pit --rm -p1337:1337 -p3000:3000 -it web_dox_pit