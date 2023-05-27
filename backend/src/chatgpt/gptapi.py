import openai

from src.domain.question import question_schema
from src.chatgpt import prompt


def get_answer(_question: question_schema.QuestionCreate):

    openai.api_key = prompt.OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model=prompt.model,
        messages=prompt.get_message(_question.mbti, _question.content)
    )

    answer = response['choices'][0]['message']['content']
    return answer

