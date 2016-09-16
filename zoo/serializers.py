from rest_framework import serializers
from django.contrib.auth.models import User
from zoo.models import *

# Using the HyperlinkedModelSerializer will examine the relationships
# between the models, and the data, and provide a hyperlink to the
# related resource instead of the primary key
#   http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/#hyperlinking-our-api
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Employee
    fields = ('id', 'url', 'first_name', 'last_name', 'habitat')


class AnimalSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Animal
    fields = ('id', 'url', 'name', 'purchased', 'habitat')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'tickets', 'visitor')


class TicketSerializer(serializers.HyperlinkedModelSerializer):
  owner = UserSerializer()

  class Meta:
    model = Ticket
    fields = ('id', 'url', 'owner', 'purchased', 'habitat')



class VisitorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Visitor
        fields = ('id', 'url', 'user', 'age', 'gender')


class HabitatSerializer(serializers.HyperlinkedModelSerializer):
  # Uncomment out the following lines to see how the representation
  # of the list of related information changes in the JSON. It will
  # use the __str__ value of the object instance that you specify
  # in models.py.
  #
  # animals = serializers.StringRelatedField(many=True)
  # employees = serializers.StringRelatedField(many=True)

  # Specifying the specific serializer for a nested relationship (i.e. a
  # list of items in a one-to-many relationship) will put the full object
  # representation in the list instead of just the URI. Comment out the
  # following lines to see it in action.
  #
  # employees = EmployeeSerializer(many=True, read_only=True)
  # animals = AnimalSerializer(many=True, read_only=True)

  class Meta:
    model = Habitat
    fields = ('id', 'url', 'name', 'created', 'animals', 'employees', 'tickets')















