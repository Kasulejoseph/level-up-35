from flask import Blueprint,Flask
app = Flask(__name__)
main = Blueprint('main', __name__)
from . import views