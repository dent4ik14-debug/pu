from django.urls import path
from service.views import ServiceListView
from service.views import IndexView, MasterServiceListView

app_name = 'service'

urlpatterns = [
    path('catalog/', ServiceListView.as_view(), name='catalog'),
    path('', IndexView.as_view(), name='index'),
    path('service/<int:pk>/', MasterServiceListView.as_view(), name='service'),
]