from rest_framework import serializers
from zoo.models import Animal, Habitat, Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Employee
    fields = ('id', 'url', 'first_name', 'last_name', 'habitat')


class AnimalSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Animal
    fields = ('id', 'url', 'name', 'purchased', 'habitat')


class HabitatSerializer(serializers.HyperlinkedModelSerializer):
  # Uncomment out the following lines to see how the representation
  # of the list of related information changes in the JSON
  #
  # animals = serializers.StringRelatedField(many=True)
  # employees = serializers.StringRelatedField(many=True)

  # Specifying the serializer for a nested relationship (i.e. a list of items
  # in a one-to-many relationship) will put the full object representation
  # in the list instead of just the URI
  #
  employees = EmployeeSerializer(many=True, read_only=True)
  animals = AnimalSerializer(many=True, read_only=True)

  class Meta:
    model = Habitat
    fields = ('id', 'url', 'name', 'created', 'animals', 'employees')

