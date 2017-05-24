from django.conf.urls import url

from flight import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^status/', views.all_ec2_status, name='all_ec2_status'),
]