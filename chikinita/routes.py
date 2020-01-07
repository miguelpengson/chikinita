from flask import render_template, url_for, flash, redirect, request
from chikinita import app, db, bcrypt
from chikinita.forms import RegistrationForm, LoginForm
from chikinita.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()  # from forms.py (class)
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in.', 'success') # success is bootstrap
        return redirect(url_for('login'))   # login is our function
    return render_template('register.html', title='Register', form=form)
 
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')