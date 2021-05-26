from app import app
from flask import render_template
from app.models import Post

#Testing- bsing around trying to add in features
#Development- set to development server not the real server
#Production - live

@app.route('/')
def home():
    return render_template('index.html')


#MVC FRAMEWORK- MODEL, VIEW CONTROL
@app.route('/contact')
def contact():
    context = {
        'help': 'yes',
        'page': 1,
        'yellow': 'jaune'
    }
    return render_template('contact.html')

@app.route('/blog')
def blog():
    Post._list.clear()
    p1 = Post(1, 'https://picsum.photos/1000/500/1', 'derekh@codingtemple.com', 'Fisrt Blog Post', 'This is the body of the First Post')
    p2 = Post(2, 'https://picsum.photos/1000/500/2', 'samd@codingtemple.com', 'Second Blog Post', 'This is the body of the Second Post')
    p3 = Post(3, 'https://picsum.photos/1000/500/3', 'samd@codingtemple.com', 'Third Blog Post', 'This is the body of the Third Post')
    context = {
        'posts': [p.to_dict() for p in Post._list]
    }
    return render_template('blog.html', **context)
