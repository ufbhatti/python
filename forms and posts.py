# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 18:02:45 2025

@author: test
"""

from flask import Flask,render_template
from flask import request

app=Flask(__name__)
@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        username=request.form['username']
        return f"Hello,{username}!"
    return render_template('form.html')

if __name__=='__main__':
    app.run(debug=True)