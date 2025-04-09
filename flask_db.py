# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 19:33:31 2025

@author: test
"""



from flask import Flask, request 
import sqlite3 
app = Flask(__name__ ) 
def init_db():
    conn = sqlite3.connect('simple.db') 
    c = conn.cursor() 
    c.execute('''
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL
            )
        ''')
    conn.commit() 
    conn.close() 

@app.route('/', methods=['GET', 'POST']) 
def home(): 
    if request.method == 'POST':
        name = request.form.get('name') 
        if name: # OnLy insert if not empty 
            conn = sqlite3.connect('simple.db') 
            c = conn.cursor() 
            c.execute('INSERT INTO people (name) VALUES (?)', (name,)) 
            conn.commit() 
            conn.close() 
    conn = sqlite3.connect('simple.db') 
    c = conn.cursor() 
    c.execute('SELECT * FROM people') 
    rows = c.fetchall() 
    conn.close() 
    
    page = "<h1>People List</h1><ul>" 
    for row in rows:
        page += f"<li>{row[1]}</li>" 
        page += "</u1><h2>Add Person</h2><form method='POST'>" 
        page += "Name: <input name='name'><input type='submit'></form>" 
        return page 
if __name__ == '__main__':
    init_db()
    app.run(debug=True) 

