from django.urls import path
from myapp import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),  # 동적 URL 처리
    path('ws/test/<str:id>/', consumers.TestConsumer.as_asgi()),
    
]
