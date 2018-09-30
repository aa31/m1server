from flask import Blueprint, render_template, session, redirect, url_for
from app import utils
from app.models import User

view_bp = Blueprint('view', __name__)


@view_bp.route('/')
def index():
    params = {'cpu': utils.getCpuState(), 'mem': utils.getMemState(), 'disk': utils.getDiskState(),
              'ip': utils.get_ip(), 'netmask': utils.get_netmask(), 'sysruntime': utils.get_stsruntime()}
    return render_template('index.html', params=params)


@view_bp.route('/login/')
def login():
    return render_template('login.html')


@view_bp.route('/config_basic')
def config_basic():
    params = utils.readJson('./app/static/json/videoParams.json')
    video_config = utils.readJson('./app/config.json')
    return render_template('config_basic.html', params=params, video_config=video_config)


@view_bp.route('/config_network/')
def config_network():
    config = utils.readJson('./app/config.json')
    return render_template('config_network.html', params = config['network'])


@view_bp.route('/config_swj')
def config_swj():
    video_config = utils.readJson('config.json')
    return render_template('config_swj.html', params=video_config['swj'])


@view_bp.route('/sys_upd')
def sys_upd():
    return render_template('sys_upd.html')


@view_bp.route('/sys_cpwd')
def sys_cpwd():
    return render_template('sys_cpwd.html')


@view_bp.route('/sys_log')
def sys_log():
    return render_template('sys_log.html')


@view_bp.route('/sys_restart')
def sys_restart():
    return render_template('sys_restart.html')


@view_bp.route('/sys_time')
def sys_time():
    return render_template('sys_time.html')


@view_bp.route('/network')
def network():
    return render_template('network.html')


@view_bp.before_request
def bf_request():
    uid = session.get('uid')
    if uid:
        pass
    else:
        pass
        # return redirect(url_for("view.login"))


# @view_bp.context_processor
# def my_context_processor():
#     uid = session.get('uid')
#     if uid:
#         user = User.query.filter(User.id == uid).first()
#         if user:
#             return {'user':user}
#     return {}