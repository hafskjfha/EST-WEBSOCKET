# TEST-WEBSOCKET

## Description
웹소켓 구현 연습 및 연습사용<br>
.venv사용 권장
```bash
python -m venv .venv
.venv\Scripts\activate
```

## Module
- channels 
- django

### pip
```bash
pip install -r requirements.txt
```

## Run

### Web Socket
```bash
$ daphne -b 127.0.0.1 -p 8001 myproject.asgi:application
```
주소
```
ws://127.0.0.1:8001
```


### Web server
이것은 필수가 아니지만 테스트로 웹서버를 접속해서 테스트 가능 ->(templates/chat_room.html) 확인

```bash
$ python manage.py runserver
```
주소:
```
http://localhost:8000/chat/
```

## Code
### Commonness
myproject/settings.py

### Web Socket
myapp/routing.py <br>
myapp/consumers.py <br>
myproject/asgi.py <br>
### Web Server
myapp/views.py <br>
myproject/urls.py <br>
myproject/templates/...

