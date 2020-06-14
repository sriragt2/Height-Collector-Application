# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:51:08 2019

@author: Srirag
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template("home.html")

@app.route('/about/')

def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)