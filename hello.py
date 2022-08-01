#!/usr/bin/env python3

# Документация по библиоткее
# https://pymorphy2.readthedocs.io/en/stable/user/grammemes.html

from flask import Flask, request
import pymorphy2


morph = pymorphy2.MorphAnalyzer()

def create_app():
    app = Flask(__name__)

    @app.route('/<word>')
    def hello_world(word: str):
        mp = morph.parse(word)[0]
        hz = mp.inflect({'gent'}) # Родительный падеж
        return str(hz.word)

    @app.route('/2/<word>')
    def hello_world2(word: str):
        mp = morph.parse(word)[0]
        options = {'ablt'}
        if 'plur' in request.args:
            options.add('plur')
        hz = mp.inflect(options) # Творительный падеж
        return str(hz.word)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0')
