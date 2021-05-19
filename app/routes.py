from app import app
from flask import render_template

#Testing- bsing around trying to add in features
#Development- set to development server not the real server
#Production - live

@app.route('/')
def home():
    return render_template('index.html')


#MVC FRAMEWORK- MODEL, VIEW CONTROL
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')