from flask import Flask
from .main.views import main
app = Flask(__name__)
app.register_blueprint(main)
