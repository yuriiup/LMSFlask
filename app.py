from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index/<title>')
def index(title):
    return render_template('index.html', title=title)


@app.route('/traning/<profession>')
def prof(profession):
    return render_template('traning.html', profession=profession)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
