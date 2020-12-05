from sanic.request import Request
from sanic.response import json
from sanic import Blueprint
from src.controllers.users import UsersController

users = Blueprint('content_users', url_prefix='/users')

@users.middleware #interceptar as requisições desse blueprint
async def middleware(request: Request):
    print('to no middleware')


@users.get('/')
async def index(request: Request) -> json:
    return await UsersController.index(request)

@users.get('/<uid>')
async def show(request: Request, uid: str):
    return await UsersController.show(request, uid)

@users.post('/')
async def store(request: Request):
    return await UsersController.store(request)

@users.put('/<uid>')
async def update(request: Request, uid: str):
    return await UsersController.update(request, uid)

@users.delete('/<uid>')
async def destroy(request: Request, uid: str):
    return await UsersController.destroy(request, uid)

