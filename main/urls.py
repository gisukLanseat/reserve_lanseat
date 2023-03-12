from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name="main"),
    path('<int:number>/<str:room_id>', views.start, name='start'),
    path('reserve/<int:number>', view=views.reserve, name="reserve")
]