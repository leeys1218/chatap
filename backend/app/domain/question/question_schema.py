import datetime
from pydantic import BaseModel, validator


class Question(BaseModel):
    id: int
    mbti: str
    content: str
    create_date: datetime.datetime


class QuestionCreate(BaseModel):
    mbti: str
    content: str

    @validator('mbti', 'content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
