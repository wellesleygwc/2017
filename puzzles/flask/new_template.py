from flask import Flask, render_template
app = Flask(__name__)

"""
Copy this file to your directory, then modify it to put
the HTML into templates/hello.html and then the return statement
calls render_template.
You'll need to create the templates directory.
"""
@app.route('/hello')
def hello():
  return """
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Hello</title>
  </head>
  <body>
  Hello, world!
  </body>
  </html>"""

if __name__ == '__main__':
  app.run()
