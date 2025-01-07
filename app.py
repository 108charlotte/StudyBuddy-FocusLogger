# this is CHATGPT starter code for creating a basic flask application

from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define a basic route
@app.route('/')
def hello_world():
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
