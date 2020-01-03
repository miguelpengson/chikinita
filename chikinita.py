
from flask import Flask
app = Flask(__name__)    # so flask knows where to find our files
                         # instantiate Flask
@app.route("/")
@app.route("/home")
def home():
    return 'Welcome to Chikinita.com !'

@app.route("/about")
def about():
    return 'About Chikinita.com'







# setting envioronment variables
if __name__ == '__main__':
    app.run(debug=True)
