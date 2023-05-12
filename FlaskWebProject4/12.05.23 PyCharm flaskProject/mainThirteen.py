from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def home():
    return 'Hello, Flask Session!'


@app.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1
    return "Total visits: {}".format(session.get('visits'))


@app.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None)
    return 'Visits deleted'


@app.route('/session/')
def updating_session():
    res = str(session.items())

    cart_item = {'pineapples': '10', 'apples': '20', 'mangoes': '30'}
    if 'cart_item' in session:
        session['cart_item']['pineapples'] = '100'
        session.modified = True
    else:
        session['cart_item'] = cart_item

    return res


if __name__ == '__main__':
    app.run()
