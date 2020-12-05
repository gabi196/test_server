from src.database.database import BaseModel
from datetime import datetime

import peewee

class User(BaseModel):
    name = peewee.CharField()
    email = peewee.CharField()
    age = peewee.IntegerField()
    password = peewee.CharField()
    
    createdAt = peewee.DateTimeField(default=datetime.utcnow)
    updatedAt = peewee.DateTimeField(default=datetime.utcnow)
