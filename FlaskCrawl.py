from flask import Flask, request, render_template
from crawl import start

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/', methods=['POST'])
def my_form_post():
    out = ""
    text = request.form['text']
    processed = text.upper()
    urlList = start(processed)
    out += "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css' integrity='sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ' crossorigin='anonymous'><script src='https://code.jquery.com/jquery-3.1.1.slim.min.js' integrity='sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n' crossorigin='anonymous'></script><script src='https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js' integrity='sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb' crossorigin='anonymous'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js' integrity='sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn' crossorigin='anonymous'></script>"
    out += "<br><div id='header'><h1>Results for " + processed + "</h1></div>"
    out += "<div id='list'><ul class='list-group'>"
    for url in urlList:
        out += "<li class='list-group-item'>" + url + "</li>"

    out += "</ul></div>"
    out += "<style>#header {font-family: Consolas; text-align: center; margin: auto} #list {padding: 50px}</style>"
    return out

if __name__ == '__main__':
    app.run()
