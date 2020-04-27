import falcon
from src.middlewares import CORSMiddleware

app = falcon.API(middleware=[
    CORSMiddleware()
])

import src.endpoints  # NOQA
