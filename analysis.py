import tweepy


def analyse_tweets(api, tweets):
    for tweet in tweepy.Cursor(api.search, q='wildfire').items(10):
        print(tweet.retweet_count)
    # print("hi")
    return "ok"
