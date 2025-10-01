from django.urls import path,re_path,include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('<year>/<int:month>/<slug:day>',views.mydate,name='mydate'),
    path('turnTo', RedirectView.as_view(url='/'),name='turnTo'), 
    # path('', views.index2, {'month':'2019/10/10'}),
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html',views.mydate, name='mydate'),
]
