from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.web.errors import handlers
