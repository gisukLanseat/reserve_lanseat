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
]