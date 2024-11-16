import asyncio
import websockets
import json

async def send_message():
    uri = "ws://127.0.0.1:8001/ws/test/1/"  # WebSocket 서버 URL

    try:
        # 서버에 연결
        async with websockets.connect(uri) as websocket:
            # 서버와 연결된 후 메시지 보내기
            message_data = {
                "message": "Hello, WebSocket Server!"
            }
            
            # JSON 형식으로 메시지를 직렬화하여 전송
            message_json = json.dumps(message_data)
            await websocket.send(message_json)
            print(f"Sent message: {message_json}")
            
            # 서버로부터 응답 받기
            response = await websocket.recv()
            print(f"Received response: {response}")

    except Exception as e:
        print(f"Error: {e}")

# 이벤트 루프 실행
asyncio.get_event_loop().run_until_complete(send_message())
