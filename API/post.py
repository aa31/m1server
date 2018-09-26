from flask import Blueprint, request
import json
import func

# from models import User

bp = Blueprint('post',__name__)

@bp.route('/reconfig_video', methods=['GET','POST'])
def reconfig_video():
    # print(request.values )
    jsonData = func.readJson('config.json')
    reqJson = request.form
    if reqJson['resolution']:
        jsonData['video']['resolution'] = reqJson['resolution']
    if reqJson['resolution']:
        jsonData['video']['coltype'] = reqJson['coltype']
    func.createJson('config.json', jsonData)
    return json.dumps(jsonData)


@bp.route('/reconfig_swj', methods=['GET','POST'])
def reconfig_swj():
    jsonData = func.readJson('config.json')
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
    func.createJson('config.json', jsonData)
    return json.dumps(jsonData)