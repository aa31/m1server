from flask import Blueprint
# from models import User

bp = Blueprint('post',__name__)

@bp.route('/reconfig_swj')
def reconfig_swj():

    return 'User.query.all()'
