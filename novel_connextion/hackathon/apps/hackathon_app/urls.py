from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^result_process$', views.result_process),
    url(r'^results$', views.results)   
]                            
