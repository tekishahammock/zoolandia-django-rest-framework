from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from zoo.models import Animal, Habitat, Employee
from zoo.serializers import AnimalSerializer, HabitatSerializer, EmployeeSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        "animals": reverse("animal-list", request=request, format=format),
        "habitats": reverse("habitat-list", request=request, format=format),
        "employees": reverse("employee-list", request=request, format=format)
    })

class AnimalList(viewsets.ModelViewSet):
    model = Animal
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalDetail(viewsets.ModelViewSet):
    model = Animal
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = 'name'


class HabitatList(viewsets.ModelViewSet):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer

class HabitatDetail(viewsets.ModelViewSet):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer
    lookup_field = 'name'


class EmployeeList(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'last_name'


