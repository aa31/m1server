# coding=utf-8
from flask import Flask, render_template
import psutil
import socket,time, datetime
app = Flask(__name__)


# 返回ip
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


# 获取网卡名称和其ip地址，不包括回环
def get_netcard():
    netcard_info = []
    info = psutil.net_if_addrs()
    for k,v in info.items():
        for item in v:
            if item[0] == 2 and not item[1]=='127.0.0.1':
                netcard_info.append((k,item[1]))
    return netcard_info


@app.route('/')
def index():
    # netaddrs = get_netcard()
    return render_template('index.html', ip='11')


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
    app.run(port=9909)