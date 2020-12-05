from json import JSONEncoder
from datetime import datetime

class Serialize(JSONEncoder):
    def default(self,field):
        if isinstance(field, datetime):
            return field.isoformat() + 'Z'