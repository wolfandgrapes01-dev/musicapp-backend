from fastapi import FastAPI

from api.routes import auth_router, otp_router, playlist_router

app = FastAPI()

app.include_router(auth_router.router, prefix='/auth')

app.include_router(playlist_router.router, prefix='/create')

#Base.metadata.create_all(engine)