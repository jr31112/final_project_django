from django.urls import path
from . import views
urlpatterns = [
    path('<int:user_id>/', views.user_detail, name='user_detail'),
    path('', views.signup, name='signup'),
]
