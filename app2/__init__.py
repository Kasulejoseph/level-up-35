from flask import Flask
from app2.main.views import main
app = Flask(__name__)
app.register_blueprint(main)
