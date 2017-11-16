from flask import Flask
app = Flask(__name__)

"""
Copy this file to your directory, then modify it so that
going to "/name" displays your name on the web page.
"""
@app.route('/')
def hello():
  return 'Hello, World!'

if __name__ == '__main__':
  app.run()
