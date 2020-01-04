from flask import Flask, render_template, url_for
app = Flask(__name__)    # so flask knows where to find our files
                         # instantiate Flask

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







# setting envioronment variables
if __name__ == '__main__':
    app.run(debug=True)
