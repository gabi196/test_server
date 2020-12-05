from sanic import Sanic 
from sanic_cors import CORS
from src.routes.routes import routes
from asyncio import AbstractEventLoop
from src.database.database import postgres
from peewee import IntegrityError, ProgrammingError
from src.models.user import User
app = Sanic(__name__)
CORS(app) #aceitar requisição externa
app.blueprint(routes)


@app.listener('before_server_start')
@postgres.atomic()
async def creatTables(server: Sanic, loop: AbstractEventLoop):
    try:
        postgres.create_tables([
            User
        ])
    except IntegrityError as e:
        pass
    except ProgrammingError as e:
        pass 
