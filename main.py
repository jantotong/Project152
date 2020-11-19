# -*- coding: utf-8 -*-
from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("record.html")

@app.route('/upload', methods=['POST'])
def upload():
    word = request.args.get('word')
    trial_number = request.args.get('trialN')
    name = request.args.get('name')
    
    return


if __name__ == "__main__":
    app.run(threaded=True, port=80)
