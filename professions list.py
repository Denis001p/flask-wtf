from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/list_prof/<list>')
def training(list):
    param = {}
    param['list'] = list
    param['profs'] = []
    return render_template('training.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
