from rest_framework import routers
from django.conf.urls import url, include
from zoo import views

router = routers.DefaultRouter()
router.register(r'animals', views.AnimalList)
router.register(r'habitats', views.HabitatList)
router.register(r'employees', views.EmployeeList)

urlpatterns = [
    url(r'^', include(router.urls)),
]

# urlpatterns = [
#     url(r'^$', views.api_root),
#     url(r'^animals/$', views.AnimalList.as_view(), name='animal-list'),
#     url(r'^animals/(?P<pk>[0-9]+)/$', views.AnimalDetail.as_view(), name='animal-detail'),
#     url(r'^habitats/$', views.HabitatList.as_view(), name='habitat-list'),
#     url(r'^habitats/(?P<pk>[0-9]+)/$', views.HabitatDetail.as_view(), name='habitat-detail'),
#     url(r'^employees/$', views.EmployeeList.as_view(), name='employee-list'),
#     url(r'^employees/(?P<pk>[0-9]+)/$', views.EmployeeDetail.as_view(), name='employee-detail'),
# ]