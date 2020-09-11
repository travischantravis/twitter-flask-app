from flask import Flask, render_template
import tweepy

# Set-up
app = Flask(__name__)
app.config.from_pyfile('envvar.py')
TWITTER_API_KEY = app.config.get("TWITTER_API_KEY")
TWITTER_API_KEY_SECRET = app.config.get("TWITTER_API_KEY_SECRET")


# Home route
@app.route("/")
@app.route("/hello/<name>")
def home_page(name="Travis"):
    return render_template('index.html', name=TWITTER_API_KEY_SECRET)
