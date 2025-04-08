# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 17:46:36 2025

@author: test
"""

from flask import Flask,render_template


app=Flask(__name__)

#our data
@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"

@app.route('/')
def home():
    return "Heelo to the Flask"
@app.route('/about')
def about():
    return"this is the about page"
    
@app.route('/contact')
def contact():
    return"This is the Contact page"

@app.route('/hello/<name>')
def hello(name):
    return render_template('new.html',name=name)


#default file
if __name__=='__main__':
    app.run(debug=True)
    