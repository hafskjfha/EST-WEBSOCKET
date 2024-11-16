import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import myapp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP 요청
    "websocket": AuthMiddlewareStack(  # WebSocket 요청
        URLRouter(
            myapp.routing.websocket_urlpatterns  # myapp.routing에 정의된 URL 패턴 사용
        )
    ),
})
