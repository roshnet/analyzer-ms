import json
from src import app


class DefaultResource:
    def on_get(self, req, resp):
        resp.media = json.dumps({
             "status": "pass"
        })


app.add_route("/api/v1", DefaultResource())
