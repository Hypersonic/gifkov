from flask import Flask, render_template
from urllib2 import urlopen
import json

app = Flask(__name__)

api_key = "dc6zaTOxFJmzC"

def keyword_for_tweet_text(text):
    """ Return a keyword representing a tweet's essence.
        Currently the longest word in the tweet
    """
    return max(text.split(), key=len)

def get_img_url(text):
    u = urlopen("http://api.giphy.com/v1/gifs/translate?s=" + "+".join(text.split()) + "&api_key=" + api_key)
    res = json.loads(u.read())
    return res['data']['images']['fixed_height']['url']

@app.route('/')
def index():
    d = {}
    d['url'] = get_img_url('cat')
    d['search'] = 'cat'
    return render_template('home.html', d=d)

if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)
