from flask import Blueprint


demandApp = Blueprint('demandApp', __name__)
from . import views
