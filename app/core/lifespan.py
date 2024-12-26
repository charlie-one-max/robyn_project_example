from app.core.db import db_init


async def startup_handler():
    await db_init()
    print("Starting up")


async def shutdown_handler():
    print("Shutting down")
