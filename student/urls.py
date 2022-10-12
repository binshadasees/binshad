from django.urls import path
from . import views
app_name='student'
urlpatterns = [
    path('change_password', views.home,name='password'),
    path('local',views.local,name='leagel')
]