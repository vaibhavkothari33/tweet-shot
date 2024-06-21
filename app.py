# from flask import Flask, request, jsonify, render_template
# import tweepy
# app = Flask(__name__)

# # Twitter API credentials
# API_KEY = '7jI1CbrUUqFMhaDGpOvnrWG5l'
# API_SECRET_KEY = 'NcaYv3M92syUJS6nisHK5AFBZh8YWCUsE8Q2fph4XdDQ3FTdYg'
# ACCESS_TOKEN = '1740968050629758977-NrnXJG0r7UBY5Hoft6w3ibTvKOy7cv'
# ACCESS_TOKEN_SECRET = '8SjmqM9xHjk4IsET9xIHzUk2l6RoQzaxilypse8td2GgV'

# # Set up Tweepy API
# auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

# def get_tweet_content(tweet_url):
#     tweet_id = tweet_url.split('/')[-1]
#     tweet = api.get_status(tweet_id, tweet_mode='extended')
#     return {
#         "text": tweet.full_text,
#         "likes": tweet.favorite_count,
#         "retweets": tweet.retweet_count,
#         "author": tweet.user.screen_name,
#         "author_image": tweet.user.profile_image_url
#     }

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/fetch_tweet', methods=['POST'])
# def fetch_tweet():
#     tweet_url = request.json['url']
#     tweet_data = get_tweet_content(tweet_url)
#     return jsonify(tweet_data)

# if __name__ == '__main__':
#     app.run(debug=True)

# import tweepy
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Twitter API credentials
# BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAPWtuQEAAAAAyvspFyiZf2tDz6OUFzkdeLGGCx4%3DzmWVeRiAS06wra0ZPZCKPVfOzzWd8gfymFmaY1zkeRrndJSXTs'

# # Set up Tweepy API with Bearer Token
# client = tweepy.Client(bearer_token=BEARER_TOKEN)

# def get_tweet_content(tweet_url):
#     tweet_id = tweet_url.split('/')[-1]
#     tweet = client.get_tweet(tweet_id, tweet_fields=['created_at', 'public_metrics', 'text', 'author_id'], expansions=['author_id'], user_fields=['username', 'profile_image_url'])
#     tweet_data = tweet.data
#     author_data = tweet.includes['users'][0]
#     return {
#         "text": tweet_data['text'],
#         "likes": tweet_data['public_metrics']['like_count'],
#         "retweets": tweet_data['public_metrics']['retweet_count'],
#         "author": author_data['username'],
#         "author_image": author_data['profile_image_url']
#     }

# @app.route('/')
# def home():
#     return "Welcome to TweetShot!"

# @app.route('/fetch_tweet', methods=['POST'])
# def fetch_tweet():
#     tweet_url = request.json['url']
#     tweet_data = get_tweet_content(tweet_url)
#     return jsonify(tweet_data)

# if __name__ == '__main__':
#     app.run(debug=True)

# import tweepy
# from flask import Flask, redirect, url_for, request, jsonify
# from flask_dance.contrib.twitter import make_twitter_blueprint, twitter

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # Twitter API credentials
# API_KEY = '7jI1CbrUUqFMhaDGpOvnrWG5l'
# API_SECRET_KEY = 'NcaYv3M92syUJS6nisHK5AFBZh8YWCUsE8Q2fph4XdDQ3FTdYg'
# ACCESS_TOKEN = '1740968050629758977-NrnXJG0r7UBY5Hoft6w3ibTvKOy7cv'
# ACCESS_TOKEN_SECRET = '8SjmqM9xHjk4IsET9xIHzUk2l6RoQzaxilypse8td2GgV'


# # Set up Tweepy API with OAuth 1.0a User Authentication
# auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

# # Flask-Dance setup
# twitter_bp = make_twitter_blueprint(api_key=API_KEY, api_secret=API_SECRET_KEY)
# app.register_blueprint(twitter_bp, url_prefix='/twitter_login')

# @app.route('/')
# def home():
#     return "Welcome to TweetShot!"

# @app.route('/fetch_tweet', methods=['POST'])
# def fetch_tweet():
#     tweet_url = request.json['url']
#     tweet_id = tweet_url.split('/')[-1]
#     tweet = api.get_status(tweet_id, tweet_mode='extended')
#     tweet_data = {
#         "text": tweet.full_text,
#         "likes": tweet.favorite_count,
#         "retweets": tweet.retweet_count,
#         "author": tweet.user.screen_name,
#         "author_image": tweet.user.profile_image_url
#     }
#     return jsonify(tweet_data)

# @app.route('/post_tweet', methods=['POST'])
# def post_tweet():
#     if not twitter.authorized:
#         return redirect(url_for('twitter.login'))
#     tweet_content = request.json['content']
#     response = api.update_status(tweet_content)
#     return jsonify({"status": "success", "tweet_id": response.id})

# if __name__ == '__main__':
#     app.run(debug=True)


# import tweepy
# from flask import Flask, redirect, url_for, request, jsonify, session
# from requests_oauthlib import OAuth1Session

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Replace with a secure, randomly generated key

# # Twitter API credentials
# API_KEY = '7jI1CbrUUqFMhaDGpOvnrWG5l'
# API_SECRET_KEY = 'NcaYv3M92syUJS6nisHK5AFBZh8YWCUsE8Q2fph4XdDQ3FTdYg'

# # OAuth1Session setup
# oauth = OAuth1Session(API_KEY, client_secret=API_SECRET_KEY)

# # Tweepy API setup
# auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY)
# api = tweepy.API(auth)

# @app.route('/')
# def home():
#     return "Welcome to TweetShot!"

# @app.route('/login/twitter')
# def login_twitter():
#     # Obtain a request token from Twitter
#     request_token_url = 'https://api.twitter.com/oauth/request_token'
#     fetch_response = oauth.fetch_request_token(request_token_url)
    
#     # Store the request token in session for later use
#     session['request_token'] = fetch_response
    
#     # Redirect user to Twitter's authorization page
#     authorization_url = oauth.authorization_url('https://api.twitter.com/oauth/authorize')
#     return redirect(authorization_url)

# @app.route('/login/twitter/callback')
# def twitter_callback():
#     # Get the saved request token from session
#     request_token = session.pop('request_token', None)
#     if request_token is None:
#         return jsonify({"error": "Failed to retrieve request token."}), 400
    
#     # Exchange the request token for an access token
#     oauth = OAuth1Session(API_KEY,
#                           client_secret=API_SECRET_KEY,
#                           resource_owner_key=request_token['oauth_token'],
#                           resource_owner_secret=request_token['oauth_token_secret'])
    
#     access_token_url = 'https://api.twitter.com/oauth/access_token'
#     oauth_tokens = oauth.fetch_access_token(access_token_url)
    
#     # Use the obtained access tokens to authenticate with Tweepy
#     auth.set_access_token(oauth_tokens['oauth_token'], oauth_tokens['oauth_token_secret'])
#     api = tweepy.API(auth)
    
#     # Example: Fetch user details
#     user = api.me()
    
#     return jsonify({"user_id": user.id, "screen_name": user.screen_name})

# @app.route('/fetch_tweet', methods=['POST'])
# def fetch_tweet():
#     tweet_url = request.json['url']
#     tweet_id = tweet_url.split('/')[-1]
#     tweet = api.get_status(tweet_id, tweet_mode='extended')
#     tweet_data = {
#         "text": tweet.full_text,
#         "likes": tweet.favorite_count,
#         "retweets": tweet.retweet_count,
#         "author": tweet.user.screen_name,
#         "author_image": tweet.user.profile_image_url
#     }
#     return jsonify(tweet_data)

# @app.route('/post_tweet', methods=['POST'])
# def post_tweet():
#     tweet_content = request.json['content']
#     response = api.update_status(tweet_content)
#     return jsonify({"status": "success", "tweet_id": response.id})

# if __name__ == '__main__':
#     app.run(debug=True)


import tweepy
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure, randomly generated key

# Twitter API credentials (replace with your actual keys)
API_KEY = '7jI1CbrUUqFMhaDGpOvnrWG5l'
API_SECRET_KEY = 'NcaYv3M92syUJS6nisHK5AFBZh8YWCUsE8Q2fph4XdDQ3FTdYg'
ACCESS_TOKEN = '1740968050629758977-NrnXJG0r7UBY5Hoft6w3ibTvKOy7cv'
ACCESS_TOKEN_SECRET = '8SjmqM9xHjk4IsET9xIHzUk2l6RoQzaxilypse8td2GgV'


# Set up Tweepy API with OAuth 1.0a User Authentication
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetch_tweet', methods=['POST'])
def fetch_tweet():
    if request.is_json:
        tweet_url = request.json.get('url')
    else:
        tweet_url = request.form['tweetUrl']

    tweet_id = tweet_url.split('/')[-1]
    try:
        tweet = api.get_status(tweet_id, tweet_mode='extended')
        tweet_data = {
            "text": tweet.full_text,
            "likes": tweet.favorite_count,
            "retweets": tweet.retweet_count,
            "author": tweet.user.screen_name,
            "author_image": tweet.user.profile_image_url
        }
        return jsonify(tweet_data)
    except tweepy.TweepError as e:
        error_message = {"error": str(e)}
        return jsonify(error_message), 400

@app.route('/post_tweet', methods=['POST'])
def post_tweet():
    tweet_content = request.json['content']
    try:
        response = api.update_status(tweet_content)
        return jsonify({"status": "success", "tweet_id": response.id})
    except tweepy.TweepError as e:
        error_message = {"error": str(e)}
        return jsonify(error_message), 400

if __name__ == '__main__':
    app.run(debug=True)
