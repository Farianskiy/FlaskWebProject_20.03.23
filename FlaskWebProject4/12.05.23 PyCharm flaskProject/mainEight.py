from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='Jerry')


@app.route('/admin/')
def admin():
    if not loggedin:
        return redirect(url_for('login'))  # Редирект на страницу входа, если не залогинен
    return render_template('admin.html')


@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    # код обработки профиля пользователя
    return f"User Profile: {user_id}"


@app.route('/books/<genre>/')
def books(genre):
    # код обработки книг по жанру
    return f"Books by genre: {genre}"


if __name__ == '__main__':
    app.run()
