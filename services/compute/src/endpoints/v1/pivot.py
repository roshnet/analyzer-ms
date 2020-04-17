import falcon
import json
from src import app
from src.utils import prepare_pivot_payload


class PivotDataResource:
    def on_get(self, req, resp):
        column = req.params.get('about')
        payload, err = prepare_pivot_payload(column)
        if err is not None:
            resp.body = json.dumps({
                'status': 'fail',
                'error': str(err)
            })
        else:
            resp.body = json.dumps({
                'status': 'pass',
                'result': payload
            })


app.add_route('/api/v1/pivot', PivotDataResource())
