from fastapi import FastAPI

from api.routes import auth_router, otp_router

app = FastAPI()

app.include_router(auth_router.router, prefix='/auth')
app.include_router(otp_router.router, prefix='/otp')

#Base.metadata.create_all(engine)