from app import app

#Testing- bsing around trying to add in features
#Development- set to development server not the real server
#Production - live

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/contact')
def contact():
    return "This is the contact page!"

@app.route('/blog')
def blog():
    return 'This is the blog page'