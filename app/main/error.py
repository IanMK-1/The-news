from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(error):
    """Function to handle the 404 page not found error"""

    return render_template('page_not_found_error.html'), 404
