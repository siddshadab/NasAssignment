from django.conf.urls import url
from rest_framework.routers import  SimpleRouter
from restApi import views
from django.urls import include

router = SimpleRouter()
router.register(r'parkingSystem', views.get_parking)
router.register(r'check_out', views.get_check_out_details)

urlpatterns = [
    url(r'^', include(router.urls)),
]
