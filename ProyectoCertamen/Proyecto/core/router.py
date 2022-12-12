from rest_framework.routers import DefaultRouter
from core.views import EquipoApiViewSet

router_posts = DefaultRouter()

router_posts.register(prefix = 'post', basename = 'post', viewset= EquipoApiViewSet)