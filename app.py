from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def mars1():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    lines = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
             ]
    return '</br>'.join(lines)


@app.route('/image_mars')
def image_mars():
    return render_template('image_mars')


@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)