from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.conn import db
from app.domain.question import question_schema, question_crud

router = APIRouter(
    prefix="/api/question",
)


@router.post("/create")
def question_create(_question_create: question_schema.QuestionCreate,
                    session: Session = Depends(db.get_db)):
    print(_question_create)
    
    return question_crud.create_question(db=session, question_create=_question_create)


@router.post("/create_test")
def question_create(_question_create: question_schema.QuestionCreate,
                    session: Session = Depends(db.get_db)):
    print(_question_create)

    return question_crud.create_question_test(db=session, question_create=_question_create)

