from sanic.request import Request
from sanic.response import json
from src.models.user import User
from playhouse.shortcuts import model_to_dict, update_model_from_dict
from src.utils.serialize import Serialize
from json import dumps


class UsersController:
    @staticmethod
    async def index(request: Request):
        request.args
        page = 0
        size = 5
        if 'page' in request.args and request.args['page'][0].isnumeric():
            page = request.args['page'][0]
            page = int(page)

        if 'size' in request.args and request.args['size'][0].isnumeric():
            size = request.args['size'][0]

            size = int(size)
            if size not in [5, 10, 20]:
                size = 5

        query = User.select().paginate(page,paginate_by=size).limit(size)
        users = list()
        for data in query:
            user = model_to_dict(data)
            users.append(user)

        return json(users, dumps=dumps, cls=Serialize)
    
    @staticmethod
    async def show(request: Request, uid: str):
        user = User.get_or_none(id=uid)
        if user is None:
            return json({'Erro': 'Usuário não encontrado'}, status=404)
        user = model_to_dict(user)
        return json(user, dumps=dumps, cls=Serialize)
    
    @staticmethod
    async def store(request: Request):
        user = User.create(**request.json)
        user = model_to_dict(user)
        return json(user, dumps=dumps, cls=Serialize, status=201)
    
    @staticmethod
    async def update(request: Request, uid: str):
        user = User.get_or_none(id=uid)
        if user is None:
            return json({'Erro': 'Usuário não encontrado'}, status=404)

        query = User.update(**request.json).where(User.id == user.id).execute()
        user = update_model_from_dict(user, request.json)
        return json(model_to_dict(user), dumps=dumps, cls=Serialize)

    @staticmethod
    async def destroy(request: Request, uid: str):
        user = User.get_or_none(id=uid)
        if user is None:
            return json({'Erro': 'Usuário não encontrado'}, status=404)
        User.delete().where(User.id == user.id).execute()
        return json(None, status=204)