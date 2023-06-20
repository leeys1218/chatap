from datetime import datetime

from app.domain.question.question_schema import QuestionCreate
from app.database.models import Question, Answer
from sqlalchemy.orm import Session
from app.chatgpt import gptapi


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
    return answer


def create_question_test(db: Session, question_create: QuestionCreate):

    answer = "[보고서]\n이 보고서는 INFJ 유형에게 받은 질문과 고민에 대한 분석과 조언을 담고 있습니다.\n\n[분석]\nINFJ 유형은 다른 사람의 감정에 민감하고 공감능력이 뛰어나며, 사람들을 돕는 데 열심입니다. 때문에 친구와의 갈등이나 힘든 상황에서는 자신이 맞서는 것보다는 상대방의 입장과 감정을 고려하려는 경향이 있습니다. 또한, INFJ 유형은 내적으로 많은 인정과 격려가 필요합니다.\n\n[MBTI 타입과 관련한 조언]\n-친구와의 갈등: 갈등 상황에서는 감정을 억누르고 상대방의 입장을 들어보는 것이 중요합니다. 양쪽의 생각을 들어서 상황을 잘 파악하고 논리적으로 해결책을 찾는 것이 좋습니다. 그러나, 갈등이 지속된다면 상대방과 자신의 감정을 솔직하게 표현하고 서로 이해하려 노력하는 것이 좋습니다.\n-컴퓨터 공부: 힘든 공부에서는 명분이 중요합니다. 자신이 공부하는 이유와 공부 결과를 위해 투자하는 시간과 노력을 생각하면서 꾸준한 노력을 유지하는 것이 중요합니다. 유명한 심리학자 William James의 말처럼 \"의지력은 우리가 우리 자신이 원하는 대로 생각하게 만들 수 있습니다.\"\n\n[심리학의 유명 인사 인용한 조언]\n-친구와의 갈등: \"혼자서는 아무것도 할 수 없다\"는 인용문에서 알 수 있듯이, 갈등 상황에서는 상대방의 입장을 경청하고 인내심을 유지하면서 솔직하게 대화하는 것이 중요합니다. -Eleanor Roosevelt\n-컴퓨터 공부: \"의지력은 그것을 만드는 데 큰 노력이 필요하지만, 그것이 작동할 때 아무것도 불가능하지 않은 것 같다.\" -William James"

    db_question = Question(mbti=question_create.mbti,
                           content=question_create.content,
                           create_date=datetime.now())
    db_answer = Answer(question=db_question,
                       content=answer,
                       create_date=datetime.now())

    db.add(db_question)
    db.add(db_answer)
    db.commit()

    return answer
