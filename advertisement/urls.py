from django.urls import path


from .views import AdvertisementDetailView,AdvertisementListView,advertisement_list

urlpatterns = [
    path('',advertisement_list, name = 'advertisement_list'),
    path('advertisements/',AdvertisementListView.as_view(), name = 'advertisement'),
    path('advertisements/<int:pk>',AdvertisementDetailView.as_view(), name='advertisement-detail'),

]