# coding=utf-8
from flask import Flask, render_template
import psutil
import socket,time, datetime
import func

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
    return render_template('config_basic.html')


@app.route('/config_network')
def config_network():
    return render_template('config_network.html')


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


if __name__ == '__main__':
    app.run(port=9909, debug=True)