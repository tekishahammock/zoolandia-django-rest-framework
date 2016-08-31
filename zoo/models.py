from django.db import models
from django.utils import timezone


class Habitat(models.Model):
  name = models.CharField(max_length=25)
  created = models.DateTimeField(default=timezone.now)

  # This representation is used any time a base string representation
  # is needed, such as the web browseable API interface provide by
  # the framework.
  def __str__(self):
    return "{}: {}".format(self.id, self.name)

  # This representation will be used if you use StringRelatedField
  # serializers
  def __unicode__(self):
    return "{}: {}".format(self.id, self.name)


class Animal(models.Model):
  name = models.CharField(max_length=55)
  purchased = models.DateTimeField(default=timezone.now)
  habitat = models.ForeignKey(Habitat, related_name='animals')

  def __str__(self):
    return "{}: {}".format(self.id, self.name)

  def __unicode__(self):
    return "{}: {}".format(self.id, self.name)


class Employee(models.Model):
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)
  habitat = models.ForeignKey(Habitat, related_name='employees')