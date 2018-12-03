from flask import Flask, render_template
from secrets import *
import json
import requests 
app = Flask(__name__)

@app.route('/')
def index():    
    return '<h1>Welcome!</h1>'

@app.route('/user/<name>')
def user(name):
    headlines = ""
    baseurl = 'https://api.nytimes.com/svc/topstories/v2/technology.json?'
    params={'api-key': api_key}
    resp = requests.get(baseurl, params)
    texts = json.loads(resp.text)

    list_headlines = []
    i = 1
    for t in texts["results"]:
        title = t["title"] + " (" + t["url"] + ") \n"
        list_headlines.append(title)
        i+= 1
    list_headlines = list_headlines[:5]


    return render_template('user.html', name=name, headlines=list_headlines)


if __name__ == '__main__': 
    print('starting Flask app', app.name)  
    app.run(debug=True)

    