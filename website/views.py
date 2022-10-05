from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1> home </h1>"


@views.route('/add_member')
def add_member():
    return "<h1> add_member </h1>"
