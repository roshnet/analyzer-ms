import json
from src import app


class DefaultResource:
    def on_get(self, req, resp):
        resp.body = json.dumps({
             'status': 'pass'
        })


app.add_route('/api/v1', DefaultResource())
