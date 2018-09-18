from flask import Flask

app = Flask(__name__)


@app.route('/get_sysstatus')
def get_sysstatus():
    return 'sysstate'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'])
