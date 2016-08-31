from rest_framework import routers
from django.conf.urls import url, include
from zoo import views

# Django REST framework uses conventions heavily. Consider the two
# ways of defining the routes below. This first, uncommented block
# is very concise, but also makes many assumptions.
#
# The DefaultRouter will bind the route you specify (e.g. 'animals')
# with a ViewSet but also automagically creates a default / route that
# will list all of the resources you specify.
# {
#   "animals": "http://localhost:8000/animals/",
#   "habitats": "http://localhost:8000/habitats/",
#   "employees": "http://localhost:8000/employees/"
# }
#
# It uses convention to define the detail view as well, which had
# to be manually built using basic routing at the bottom. Notice that it is
# not specified how to handle the route /animals/2. The framework figures
# that out through convention.

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