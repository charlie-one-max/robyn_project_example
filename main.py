from robyn import Robyn

from app.api.user.router import user_router
from app.common.middlewares import register_middleware
from app.core.lifespan import startup_handler, shutdown_handler

app = Robyn(__file__)

register_middleware(app)
app.startup_handler(startup_handler)
app.shutdown_handler(shutdown_handler)
app.include_router(user_router)
if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8080)
