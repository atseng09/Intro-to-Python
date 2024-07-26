from flask import Flask
from app_blueprint import app_blueprint
from flask import render_template

app = Flask(__name__)
app.register_blueprint(app_blueprint)

app.run(host="0.0.0.0", port=80)