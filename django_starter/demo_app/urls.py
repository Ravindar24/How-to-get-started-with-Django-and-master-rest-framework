from django.conf.urls import url

from . import views


urlpatterns = [

    url('demo-view/',views.CustomerView.as_view())

]