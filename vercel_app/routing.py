from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import re_path
from . import consumers



application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                re_path(r"ws/loiola-app.vercel.app/<str:room_name>/", consumers.WallpaperConsumer.as_asgi()),
                #s
            ]
        )
    ),
})