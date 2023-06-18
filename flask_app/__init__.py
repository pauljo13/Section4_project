import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def get_hello():
    return render_template('index.html')

@app.route('/main')
def main():
   return render_template('main.html')

if __name__ == "__main__":
    app.run(debug=True)
