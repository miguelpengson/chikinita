from flask import render_template, url_for, flash, redirect
from chikinita import app
from chikinita.forms import RegistrationForm, LoginForm
from chikinita.models import User, Post

posts = [
    {
        'author': 'Miguel Pengson',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 2, 2020'
    },
    {
        'author': 'Roberto Pengson',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 2, 2020'
    }
]

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  # from forms.py (class)
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') # success is bootstrap
        return redirect(url_for('index'))   # index is our function
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)