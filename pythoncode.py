# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 19:27:56 2025

@author: test
"""

from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/', method=['GET,POST'])
def index():
    if request.method=='POST':
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        address=request.form['address']