from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from zoo.models import Animal, Habitat, Employee, Ticket
from zoo.serializers import *


class AnimalList(viewsets.ModelViewSet):
    model = Animal
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class AnimalDetail(viewsets.ModelViewSet):
    model = Animal
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    lookup_field = 'name'


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TicketList(viewsets.ModelViewSet):
    model = Ticket
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TicketDetail(viewsets.ModelViewSet):
    model = Ticket
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    lookup_field = 'user'

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


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

@csrf_exempt
def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Use the built-in authenticate method to verify
    authenticated_user = authenticate(
            username=req_body['username'],
            password=req_body['password']
            )

    # If authentication was successful, log the user in
    success = True
    if authenticated_user is not None:
        login(request=request, user=authenticated_user)
    else:
        success = False

    data = json.dumps({"success":success})
    return HttpResponse(data, content_type='application/json')


