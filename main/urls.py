from django.urls import path

from . import views
from .views import dashBoard

app_name = "main"

urlpatterns = [
    path('', views.index, name="main"),
    path('cancel/<str:id>', view=views.cancel, name="cancel"),
    path('<str:number>/<str:room_id>', views.start, name='start'),
    path('reserve/<str:room_id>/<str:number>', view=views.reserve, name="reserve"),
    path('dash/', view=dashBoard, name="dashboard"),
    path('api/', views.api_index, name="api_main"),
    path('api/<str:number>/<str:room_id>', views.api_start, name='api_start'),
    path('api/reserve/<str:room_id>/<str:number>', view=views.api_reserve, name="api_reserve"),
]