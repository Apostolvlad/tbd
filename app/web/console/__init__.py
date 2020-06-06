from flask import Blueprint

bp = Blueprint('console', __name__)

from app.web.console import routes
from app.web.console.routes import check_from