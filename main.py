from flask import Flask, render_template

app = Flask(__name__)


@app.route('/register')
def index():
    return render_template('register.html')


@app.route('/login')
def log():
    return render_template('login.html')


@app.route('/')
def mai():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
