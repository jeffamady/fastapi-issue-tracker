from fastapi import FastAPI
from routes.issues import router as issues_router
from middleware.timer import timer_middleware

app = FastAPI()

app.middleware("http")(timer_middleware)

app.include_router(issues_router)
