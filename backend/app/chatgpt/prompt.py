model = "gpt-3.5-turbo"

OPENAI_API_KEY = "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"

def get_message(mbti, content):
    new_message = [
        {"role": "system", "content": "넌 융 학파의 심리분석가야 많은 자료를 인용할 줄 알아\n" +
                                  "내 질문이나 고민을 요약하고 내가 어떻게 행동하면 좋은지를 보고서 형태로 작성해줘. 다음과 같은 사항을 고려해서 작성해줘.\n" +
                                  "------------중요!!!----------\n" +
                                  "- 정말 사람에게 제공하는 보고서처럼 작성  (맨 위에 [보고서])\n" +
                                  "- 분석, MBTI 타입과 관련한 설명, 심리학의 유명 인사의 말 인용한 조언으로 3가지 항목을 서술\n" +
                                  "- 모든 대답을 엄청나게 짧게 할 것(제일 중요)\n"},
        {"role": "user", "content": ""}
    ]
    new_message[1]["content"] += "\n\n\n mbti: " + mbti
    new_message[1]["content"] += "\n 질문: " + content

    print(new_message)
    return new_message


