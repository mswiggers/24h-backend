from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_eventstream import send_event
from competition.models import Lap, Group, University, HappyHour
from competition.serializers import LapSerializer, GroupSerializer, UniversitySerializer, HappyHourSerializer

@receiver(post_save, sender=Lap)
def send_lap_update_sse(sender, instance, created, **kwargs):
  serializer = LapSerializer(instance)
  send_event('test', 'update_lap', serializer.data)

@receiver(post_delete, sender=Lap)
def send_lap_remove_sse(sender, instance, **kwargs):
  serializer = LapSerializer(instance)
  send_event('test', 'remove_lap', serializer.data)

@receiver(post_save, sender=University)
def send_university_update_sse(sender, instance, created, **kwargs):
  serializer = UniversitySerializer(instance)
  send_event('test', 'update_university', serializer.data)

@receiver(post_delete, sender=University)
def send_university_remove_sse(sender, instance, **kwargs):
  serializer = UniversitySerializer(instance)
  send_event('test', 'remove_university', serializer.data)

@receiver(post_save, sender=Group)
def send_group_update_sse(sender, instance, created, **kwargs):
  serializer = GroupSerializer(instance)
  send_event('test', 'update_group', serializer.data)

@receiver(post_delete, sender=Group)
def send_group_remove_sse(sender, instance, **kwargs):
  serializer = GroupSerializer(instance)
  send_event('test', 'remove_group', serializer.data)

@receiver(post_save, sender=HappyHour)
def send_happyhour_update_sse(sender, instance, created, **kwargs):
  serializer = HappyHourSerializer(instance)
  send_event('test', 'update_happyhour', serializer.data)

@receiver(post_delete, sender=HappyHour)
def send_happyhour_remove_sse(sender, instance, **kwargs):
  serializer = HappyHourSerializer(instance)
  send_event('test', 'remove_happyhour', serializer.data)

