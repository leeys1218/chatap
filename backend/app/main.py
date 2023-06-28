from dataclasses import asdict
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.common.config import conf
from app.database import models
from app.database.conn import db
from app.domain.question import question_router


def create_app():
    """
    앱 함수 실행
    """

    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)

    # database init
    db.init_app(app, **conf_dict)
    models.Base.metadata.create_all(bind=db.engine)

    # redis init

    # middleware def
    origins = [
        "http://127.0.0.1:5173",
        "http://localhost:5173",
        "https://127.0.0.1:5173",
        "http://172.17.0.1:5173",
        "0.0.0.0",
        "https://www.chatap.me",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # router def
    app.include_router(question_router.router)

    return app


app = create_app()





