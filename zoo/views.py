from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import json

from rest_framework import permissions, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from zoo.models import Animal, Habitat, Employee, Ticket
from zoo.serializers import *
from zoo.permissions import IsOwnerOrReadOnly


class AnimalList(viewsets.ModelViewSet):
    model = Animal
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VisitorList(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class TicketList(viewsets.ModelViewSet):
    model = Ticket
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    # The reason that the create method needed to be overridden is because
    # if you look in serializers.py, you will see that the owner field of
    # the TicketSerializer uses the base serialization method instead of
    # a HyperlinkedModelSerializer. This enables the entire owner object to
    # be sent to the client - as a property of the ticket itself - instead
    # of the owner's URL (see http://localhost:8000/tickets/ for example).
    #
    # The side effect of this is that when creating a new ticket, the entire
    # owner object needed to be in the request body. Unfortunately, doing this
    # forces Django to try to create a new User object instead of just assigning
    # that user to the ticket.
    #
    # I'm unclear why this happens.
    #
    # Therefore, I needed to override that default behavior and write my own,
    # custom creation logic for a ticket.
    #
    def create(self, request):
        existing_owner = User.objects.get(id=request.data['owner'])
        existing_habitat = Habitat.objects.get(id=request.data['habitat'])

        new_ticket = Ticket(owner=existing_owner, habitat=existing_habitat)

        new_ticket.save()

        from django.core import serializers
        data = serializers.serialize("json", (new_ticket,))
        print(data)

        return Response(data, status=status.HTTP_201_CREATED)


class HabitatList(viewsets.ModelViewSet):
    queryset = Habitat.objects.all()
    serializer_class = HabitatSerializer


class EmployeeList(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
                    username=req_body['username'],
                    password=req_body['password'],
                    email=req_body['email'],
                    first_name=req_body['first_name'],
                    last_name=req_body['last_name'],
                    )

    new_user.visitor.age = req_body['age']
    new_user.visitor.gender = req_body['gender']

    # Commit the user to the database by saving it
    new_user.save()

    return login_user(request)

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


