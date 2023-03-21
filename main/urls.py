from django.urls import path

from . import views
from .views import dashBoard

app_name = "main"

urlpatterns = [
    path('', views.index, name="main"),
    path('<int:number>/<str:room_id>', views.start, name='start'),
    path('reserve/<str:room_id>/<int:number>', view=views.reserve, name="reserve"),
    path('dash/', view=dashBoard, name="dashboard"),
    path('cancel/<str:id>', view=views.cancel, name="cancel")
]