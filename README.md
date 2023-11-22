# ChatGPT 기반 심리 분석 프로그램

MBTI와 고민을 입력 받고 분석 심리학 기반의 답변을 제공하는 웹 서비스입니다.

<br>

### RUN
<img src="https://github.com/leeys1218/chatap/assets/95534831/f34e9c39-a753-4082-b38a-b0f78ad17341" width="300" height="500"/>
<img src="https://github.com/leeys1218/chatap/assets/95534831/53a49ea1-0ff0-4869-b699-6281e2d92224" width="300" height="500"/>

<br>
<br>

### Build Local
#### Docker
##### Front End
```
** /frontend

docker . -t frontend
```
##### Back End
```
** /backend/app/chatgpt/promp.py에 다음을 추가 & config.py 클라우드 관련 설정

OPENAI_API_KEY=xxxxxxxx
```
```
** /backend

docker . -t backend
```

<br>

### Environment
- Node 16.17.0 (window)
- Python 3.10.9 (window)

### Framework
- Frontend: Svelt (nodeJS)
- Backend: FastAPI (python)
- Cloud: AWS EC2, AWS RDS
- CICD: Github action, docker-compose




