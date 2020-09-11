from flask import Flask, render_template, redirect, request, session
import tweepy

# Flask set-up
app = Flask(__name__)
app.config.from_pyfile('envvar.py')
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Twitter API set-up
consumer_key = app.config.get("TWITTER_API_KEY")
consumer_secret = app.config.get("TWITTER_API_KEY_SECRET")
callback = 'http://127.0.0.1:5000/callback'

# Home page
@app.route("/")
def home_page(name="Travis"):
    return render_template('index.html', name=name)

# Get authorization in Twitter
@app.route("/twitter")
def twitter_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
    url = auth.get_authorization_url()
    session['request_token'] = auth.request_token
    return redirect(url)

# Twitter callback
@app.route("/callback")
def twitter_callback():
    request_token = session['request_token']
    del session['request_token']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
    auth.request_token = request_token
    verifier = request.args.get('oauth_verifier')
    auth.get_access_token(verifier)
    session['token'] = (auth.access_token, auth.access_token_secret)

    return redirect('/profile')


@app.route("/profile")
def request_twitter():
    token, token_secret = session['token']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.text)
    return ender_template('profile.html',)
