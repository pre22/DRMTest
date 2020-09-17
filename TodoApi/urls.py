from django.urls import include, path
from rest_framework import routers
from TodoApi import views


router = routers.DefaultRouter()
router.register(r'heros', views.HeroViewSet)

# Wire up our using automatic URL routing
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
