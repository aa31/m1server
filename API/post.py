from flask import Blueprint, request
import json
import func

# from models import User

bp = Blueprint('post',__name__)

@bp.route('/reconfig_swj', methods=['GET','POST'])
def reconfig_swj():
    # print(request.values )
    jsonData = func.readJson('config.json')
    reqJson = request.form
    jsonData['video']['resolution'] = reqJson['resolution']
    func.createJson('config.json', jsonData)
    return json.dumps(jsonData)