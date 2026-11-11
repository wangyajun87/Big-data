# web app

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return("Hello World")

if __name__ == "__mian__":
  app.run()
  

