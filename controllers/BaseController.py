from flask import Blueprint, render_template

BaseController = Blueprint('BaseController',__name__)

@BaseController.route('/')
def index():
    return render_template('index.html')