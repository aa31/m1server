# coding=utf-8
from flask import Flask, render_template
import func
import config
import json
from API import post

app = Flask(__name__)



@app.route('/')
def index():
    params = {'cpu':func.getCpuState(),'mem':func.getMemState(),'disk':func.getDiskState(), 'ip':func.get_ip(), 'netmask':func.get_netmask(),'sysruntime':func.get_stsruntime()}
    return render_template('index.html', params=params)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/config_basic')
def config_basic():
    params = func.readJson('./static/json/videoParams.json')
    video_config = func.readJson('config.json')
    return render_template('config_basic.html', params = params, video_config = video_config)


@app.route('/config_network')
def config_network():
    return render_template('config_network.html')


@app.route('/config_swj')
def config_swj():
    return render_template('config_swj.html')


@app.route('/sys_upd')
def sys_upd():
    return render_template('sys_upd.html')


@app.route('/sys_cpwd')
def sys_cpwd():
    return render_template('sys_cpwd.html')


@app.route('/sys_log')
def sys_log():
    return render_template('sys_log.html')


@app.route('/sys_restart')
def sys_restart():
    return render_template('sys_restart.html')
    

@app.route('/sys_time')
def sys_time():
    return render_template('sys_time.html')


@app.route('/network')
def network():
    return render_template('network.html')
	
	
@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/get_sysstatus', methods=['POST'])
def get_sysstatus():
    params = {'cpu':func.getCpuState(), 'mem':func.getMemState(), 'disk':func.getDiskState()}
    return json.dumps(params)


@app.route('/getAllConfig', methods=['POST'])
def getAllConfig():
    return json.dumps(func.readJson("config.json"));


app.register_blueprint(post.bp)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(config)
app.config['JSON_AS_ASCII'] = False


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'])


