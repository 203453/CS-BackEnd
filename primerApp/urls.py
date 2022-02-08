

from django.urls import path, include, re_path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from creacionUsuarios.api import UserAPI

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    re_path(r'^api/v1/login', include('Login.urls')), 
    re_path(r'^api/v1/primer_componente/', include('primerComponente.urls')),
    re_path(r'^api/v1/loadImage/', include('loadImage.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/create_user/', UserAPI.as_view(), name = "api_create_user")
]