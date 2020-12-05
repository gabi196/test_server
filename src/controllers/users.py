from sanic.request import Request
from sanic.response import json


class UsersController:

    @staticmethod
    async def index(request: Request):
        request.json['msg'] = 'listando todos os usuários'
        return json(request.json)
    
    @staticmethod
    async def show(request: Request, uid: str):
        request.json['msg'] = f'listando o usuário: {uid}'
        return json(request.json)
    
    @staticmethod
    async def store(request: Request):
        request.json['msg'] = 'Criando um usuário'
        return json(request.json)
    
    @staticmethod
    async def update(request: Request, uid: str):
        request.json['msg'] = f'editando o usuário: {uid}'
        return json(request.json)

    @staticmethod
    async def destroy(request: Request, uid: str):
        request.json['msg'] = f'excluindo o usuário: {uid}'
        return json(request.json)