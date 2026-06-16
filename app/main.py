from fastapi import FastAPI
from routes.issues import router as issues_router
from middleware.timer import timer_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.middleware("http")(timer_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credential=True,
    allow_headers=["*"],
)

app.include_router(issues_router)
