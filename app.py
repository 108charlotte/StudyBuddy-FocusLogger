# this is CHATGPT starter code for creating a basic flask application

from flask import Flask, render_template
from flask_bcrypt import Bcrypt

import sqlite3

# Initialize the Flask application
app = Flask(__name__)

bcrypt = Bcrypt(app)

def create_database(): 
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, hash text not null);''')

# add new user: hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
# check password for authentication: bcrypt.check_password_hash(hashed_password)

# Define a basic route
@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/login')
def login(): 
    return render_template('login.html')

@app.route('/home', methods=["GET", "POST"])
def home(): 
    if request.method == 'GET': 
        return render_template('index.html')
    elif request.method == 'POST': 
        return render_template('index.html')
    

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
