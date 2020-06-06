from flask import Blueprint

bp = Blueprint('table', __name__)

from app.web.table import routes
