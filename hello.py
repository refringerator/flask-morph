from flask import Flask
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

app = Flask(__name__)

@app.route('/<word>')
def hello_world(word: str):
    mp = morph.parse(word)[0]
    hz = mp.inflect({'gent'})
    return str(hz.word)

