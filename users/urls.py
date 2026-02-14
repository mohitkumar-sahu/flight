from django.urls import path
from users import views

urlpatterns = [
    path('',views.AllStatusList.as_view())
]

