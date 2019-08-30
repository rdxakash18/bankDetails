from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from frame.frame_api import NoteViewSet




router = routers.DefaultRouter()
router.register(r'bankDetails', NoteViewSet)
urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^', include('frame.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/',include(router.urls))
]