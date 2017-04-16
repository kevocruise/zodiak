import os
import sys

sys.path.append(os.getcwd().replace('www/flask', ''))

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'www', 'templates'))

import zodiac

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_input():
    text = request.form['text']
    return zodiac.zodiac(message=text)


if __name__ == '__main__':
    app.run()
