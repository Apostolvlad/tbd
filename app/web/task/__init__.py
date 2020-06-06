from flask import Blueprint

bp = Blueprint('task', __name__)

from app.web.task import routes