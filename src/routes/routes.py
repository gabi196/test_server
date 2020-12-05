from sanic import Blueprint
from .users.users import users

routes = Blueprint.group([users])