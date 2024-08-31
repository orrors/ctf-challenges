from flask import Flask, redirect

# Simple flask server, on the first call it returns a 200 code with some content to trick the safeurl endoint
# The second time we perform the redirect

app = Flask(__name__)
n = 0

@app.route("/")
def route():
  global n
  n += 1
  if (n > 1):
    return redirect('http://localhost:1337/secret', code=301)
  else:
    return 'FAKED'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
