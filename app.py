# this is CHATGPT starter code for creating a basic flask application

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define a basic route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
