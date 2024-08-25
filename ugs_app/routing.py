from django.urls import path,re_path
from .consumers import WSArena

ws_urlpatterns =[
    # path('ws/arena/<str:game_id>',WSArena.as_asgi())
    re_path(r'^ws/arena/<str:game_id>',WSArena.as_asgi())
]
