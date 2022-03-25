from django.urls import path
from app_users.views import NewLoginView,AnotherLoginView,NewLogoutView
from app_users.views import register_view, another_register_view

urlpatterns = [
    path('login/',NewLoginView.as_view(),name='login'),
    path('another_login/',AnotherLoginView.as_view(),name='another_login'),
    path('logout/',NewLogoutView.as_view(),name='logout'),
    path('register/',register_view,name='register'),
    path('register/',register_view,name='register'),
    path('another_register/',another_register_view,name='register'),
]