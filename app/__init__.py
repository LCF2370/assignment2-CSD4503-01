from flask import Flask, render_template, jsonify

flask_app = Flask(__name__, template_folder='../templates')

from app import routes