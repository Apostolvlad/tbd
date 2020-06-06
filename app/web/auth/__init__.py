from flask import Blueprint

bp = Blueprint('auth', __name__)

#from app.web.auth import routes
from app.web.auth import routes
