model = "gpt-3.5-turbo"

OPENAI_API_KEY = "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"

messages = [
    {"role": "system", "content": "넌 융 학파의 심리분석가야 많은 자료를 인용할 줄 알아"},
    {"role": "user", "content": "내 질문을 보고 내 심리 상태의 문제점을 찾아줘.\n"
                                "다음과 같은 항목을 고려해서 말해줘\n" +
                                "- 말해주는 MBTI를 연관지어서 작성 \n" +
                                "- 정신 심리 분석 분야의 유명한 사람의 말을 인용할 것\n"
                                "- 짥게 3줄 정도 핵심이 잘 드러나게 \n"
                                "- 질문을 잘 기억해줘"}
]


def get_message(mbti, content):
    new_message = messages
    mbti = "\n- 내 mbti" + mbti
    content = "\n- 내 질문" + content
    new_message[1]["content"] += mbti
    new_message[1]["content"] += content
    return new_message

