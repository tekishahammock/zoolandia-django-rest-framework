from rest_framework import generics
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

class AnimalList(generics.ListCreateAPIView):
    model = Animal
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Animal
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = 'name'


class HabitatList(generics.ListCreateAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer

class HabitatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer
    lookup_field = 'name'


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'last_name'


