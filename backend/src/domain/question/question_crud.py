from datetime import datetime

from src.domain.question.question_schema import QuestionCreate
from src.models import Question, Answer
from sqlalchemy.orm import Session
from src.chatgpt import gptapi


def create_question(db: Session, question_create: QuestionCreate):

    answer = gptapi.get_answer(question_create)

    db_question = Question(mbti=question_create.mbti,
                           content=question_create.content,
                           create_date=datetime.now())
    db_answer = Answer(question=db_question,
                       content=answer,
                       create_date=datetime.now())

    db.add(db_question)
    db.add(db_answer)
    db.commit()

