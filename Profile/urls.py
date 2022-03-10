from django.urls import re_path
#Importacion de vistas
from Profile.views import TercerTablaList, TercerTablaDetail, UserProfile


urlpatterns = [
    re_path(r'^add_user', TercerTablaList.as_view()),
    re_path(r'^user/(?P<pk>\d+)/$',TercerTablaDetail.as_view()),
    re_path(r'^update_user/(?P<pk>\d+)/$', UserProfile.as_view()),
] 