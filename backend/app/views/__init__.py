from flask import Blueprint

from app.models import User

bp = Blueprint('views', __name__)

@bp.route('/')
def index():
    print(
        User.query.all()
    )
    
    return 'Hello, world!'