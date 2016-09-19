from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Visitor(models.Model):
  age = models.IntegerField(null=True)
  gender = models.CharField(max_length=10, null=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
    return "{} {} {}".format(self.user.username, self.age, self.gender)

# Define signals so our Profile model will be automatically
# created/updated when we create/update User instances.
@receiver(post_save, sender=User)
def create_user_visitor(sender, instance, created, **kwargs):
    if created:
        Visitor.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_visitor(sender, instance, **kwargs):
    instance.visitor.save()


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


class Ticket(models.Model):
  owner = models.ForeignKey(User, related_name='tickets')
  habitat = models.ForeignKey(Habitat, related_name='tickets')
  purchased = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return "{}: {}".format(self.id, self.habitat.name)

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
