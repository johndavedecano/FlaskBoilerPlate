from flask import Blueprint, render_template

errors = Blueprint('errors',__name__)

@errors.app_errorhandler(404)
def handler_404(error):
    return render_template('errors/404.html')

@errors.app_errorhandler(500)
def handler_500(error):
    return render_template('errors/500.html')

