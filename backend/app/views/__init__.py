from flask import Blueprint

from app.models import User

bp = Blueprint('views', __name__)

@bp.route('/')
def index():    
    return [
        user.serialize()
        for user in User.query.all()
    ]
