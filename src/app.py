from sanic import Sanic 
from sanic_cors import CORS
from src.routes.routes import routes

app = Sanic(__name__)
CORS(app) #aceitar requisição externa
app.blueprint(routes)

