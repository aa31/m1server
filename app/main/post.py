from flask import Blueprint, request, make_response, jsonify, Response, session, send_file
import json, hashlib
from app import utils
from app.models import User
from io import StringIO
import xlwt, os

post_bp = Blueprint('post', __name__)


@post_bp.route('/reconfig_video', methods=['GET','POST'])
def reconfig_video():
    # print(request.values )
    jsonData = utils.readJson('config.json')
    reqJson = request.form
    if reqJson['resolution']:
        jsonData['video']['resolution'] = reqJson['resolution']
    if reqJson['resolution']:
        jsonData['video']['coltype'] = reqJson['coltype']
    utils.createJson('config.json', jsonData)
    return json.dumps(jsonData)


@post_bp.route('/reconfig_swj', methods=['GET','POST'])
def reconfig_swj():
    jsonData = utils.readJson('config.json')
    reqJson = request.form
    if reqJson['ip']:
        jsonData['swj']['ip'] = reqJson['ip']
    pass
    if reqJson['port']:
        jsonData['swj']['port'] = reqJson['port']
    pass
    if reqJson['rtsp']:
        jsonData['swj']['rtsp'] = reqJson['rtsp']
    pass
    utils.createJson('config.json', jsonData)
    return json.dumps(jsonData)


@post_bp.route('/get_sysstatus', methods=['POST'])
def get_sysstatus():
    params = {'cpu': utils.getCpuState(), 'mem': utils.getMemState(), 'disk': utils.getDiskState()}
    return json.dumps(params)


@post_bp.route('/getAllConfig', methods=['POST'])
def getAllConfig():
    return json.dumps(utils.readJson("config.json"))


@post_bp.route('/login', methods=['POST'])
def postLogin():
    user = request.form.to_dict().get("user")
    password = request.form.to_dict().get("password")
    islong = request.form.to_dict().get("islong")
    password = md5(password)
    data = User.query.filter(User.user_account==user, User.user_pwd==password).first()
    if data:
        session['uid'] = data.id
        if islong:
            session.permanent = True
        return getApi("101", None, "ok")
    else:
        return getApi("102", None, "error")
    # data = []
    # for comment in dataSql:
    #     data.append(comment.to_json())


@post_bp.route('/loginout/', methods=['POST'])
def loginout():
    session.pop('uid')
    return "{}"


@post_bp.route("/downExcel", methods=['GET'])
def downExcel():

    wb = xlwt.Workbook(encoding='utf-8')
    table = wb.add_sheet('My Worksheet')
    table.write(0,0,1)
    table.write(0, 1, 2)
    table.write(0, 2, 3)
    # wb.save('./static/temp/ex.xls')
    # response = make_response(send_file(wb))
    # response.headers["Content-Disposition"] = "attachment; filename=views.xls;"
    return wb


@post_bp.route("/reboot", methods=['GET'])
def reboot():
    os.system('sh ../sh/reboot.sh')
    return "{}"


@post_bp.route("/changenetwork/", methods=['GET'])
def changenetwork():
    os.system('sh ../sh/changenetwork.sh' + arg0 + ' ' + arg1)
    return "{}"

def getApi(code, content, msg):
    data = {'code':code, "data":content, "msg": msg}
    return jsonify(data)


def md5(str):
    hl = hashlib.md5()
    hl.update(str.encode('utf-8'))
    return hl.hexdigest()
