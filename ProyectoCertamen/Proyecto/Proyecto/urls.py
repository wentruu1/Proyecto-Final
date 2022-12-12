"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from core.models import Equipo
#from rest_framework import routers, serializers, viewsets
from core.router import router_posts

# Serializers define the API representation.
#class EquipoSerializer(serializers.HyperlinkedModelSerializer):
    #class Meta:
       # model = Equipo
        #fields = ['codigo', 'marca', 'recibido', 'matrona']

# ViewSets define the view behavior.
#class EquipoViewSet(viewsets.ModelViewSet):
    #queryset = Equipo.objects.all()
    #serializer_class = EquipoSerializer

# Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'equipos', EquipoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('informe',views.informe, name='informe'),
    path('api/', include(router_posts.urls))


]

class FlatPageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('url', 'title', 'content', 'sites')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('registration_required', 'template_name'),
        }),
    )