import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import Messages.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # handles normal HTTP requests
    "websocket": AuthMiddlewareStack(  # handles WebSocket with user sessions
        URLRouter(
            Messages.routing.websocket_urlpatterns  # your WebSocket routes
        )
    )
})
