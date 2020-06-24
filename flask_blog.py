from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '79615371aafb9487a031687d98deed6f'

posts = [
    {
        'author': 'Mark Davis',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 24, 2020'
    },
    {
        'author': 'Liz Prestia',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 25, 2020'  
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)    

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)    


#runs in debug without exporting environment variables
'''if __name__ == '__main__':
    app.run(debug=True)'''