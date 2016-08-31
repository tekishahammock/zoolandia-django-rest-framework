from django.db import models
from django.utils import timezone

# Create your models here.
class Habitat(models.Model):
  name = models.CharField(max_length=25)
  created = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return "{}: {}".format(self.id, self.name)

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