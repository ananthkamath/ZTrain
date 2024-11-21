from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Flask says Hello!!!</p>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)