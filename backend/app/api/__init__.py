from flask import Blueprint

bp = Blueprint('api', __name__)

# Import API routes
from . import routes