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


@app.route('/')
def welcome():
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

'''
<li><a href="/login">Login</a></li>
                    <li><a href="/register">Sign up</a></li>
                    {%else%}
                    <li><a href="/home">Login</a></li>
                    <li><a href="/setup_instructions">Extension Setup Instructions</a></li>
                    <li><a href="/extension_download">Extension Download</a></li>
'''