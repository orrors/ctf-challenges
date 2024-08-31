#!/bin/bash
docker build --tag=ws_todo .
docker run -p 80:80 -p 8000:8080 --rm --name=ws_todo -it ws_todo
