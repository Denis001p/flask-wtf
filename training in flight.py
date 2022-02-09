from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['title'] = 'Mars colonisation'
    return render_template('base.html', **param)


@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['prof'] = prof
    return render_template('training.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')