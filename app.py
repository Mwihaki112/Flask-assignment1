from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/about')
def about():
    return "This is my first Flask application."

@app.route('/contact')
def contact():
    return "Contact page"

if __name__ == '__main__':
    app.run(debug=True)