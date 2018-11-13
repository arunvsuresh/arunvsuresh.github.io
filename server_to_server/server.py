from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/arunvsuresh.github.io", methods=['GET', 'POST'])
def landing():
    print request
    return "Hello World!"

if __name__ == '__main__':
    app.run()