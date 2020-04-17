from django.conf.urls import url
from .views import CompanyView

urlpatterns = [
    url('', CompanyView.as_view(), name='index'),
]