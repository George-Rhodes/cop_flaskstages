from flask import Flask
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return """<html>
              <head>
                <title>home page</title>
              </head>
              <body>
                <h1>Home Page</h1>
              </body>
            </html>
        """
@app.route('/about')
def about():
    return """<html>
              <head>
                <title>about page</title>
              </head>
              <body>
                <h1>About Page</h1>
              </body>
            </html>
        """

