from django.urls import path
from app_users.views import NewLoginView,AnotherLoginView,NewLogoutView

urlpatterns = [
    path('login/',NewLoginView.as_view(),name='login'),
    path('another_login/',AnotherLoginView.as_view(),name='another_login'),
    path('logout/',NewLogoutView.as_view(),name='logout'),
]