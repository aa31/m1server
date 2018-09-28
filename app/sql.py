from flask import jsonify, Blueprint
# import config
from app.models import User2

bp = Blueprint('sql',__name__)


@bp.route('/aa')
def aa():
    dataSql = User2.query.all()
    data = []
    for comment in dataSql:
        data.append(comment.to_json())
    return jsonify(data)
