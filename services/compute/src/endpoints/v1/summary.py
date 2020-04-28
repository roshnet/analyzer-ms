import falcon
import json
from src import app
from src.utils.payload import get_summary_from_excel


class DataSummaryResource:
    def on_get(self, req, resp):
        columns, err = get_summary_from_excel()
        if err is not None:
            resp.status = falcon.HTTP_500
            resp.body = json.dumps({
                'status': 'fail',
                'error': err,
            })
        else:
            resp.body = json.dumps({
                'status': 'pass',
                'result': columns,
            })


app.add_route('/api/v1/summary', DataSummaryResource())
