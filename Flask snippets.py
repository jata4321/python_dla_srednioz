from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def bar(error):
    return render_template('error.html'), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

render_template('page.html', foo=bar)
