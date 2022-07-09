#!/usr/bin/env python3

from flask import Flask
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

app = Flask(__name__)

@app.route('/<word>')
def hello_world(word: str):
    mp = morph.parse(word)[0]
    hz = mp.inflect({'gent'})
    return str(hz.word)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
