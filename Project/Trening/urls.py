from django.conf.urls import url,include
from django.contrib import admin
from Trening import views

urlpatterns = [
    url(r'^$',views.basic_view,name="base"),
    url(r'^receive_request$',views.Request_Handler,name="Request_handler"),
]