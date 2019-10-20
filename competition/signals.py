from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_eventstream import send_event
from competition.models import Lap, Group, University, HappyHour, GroupScore, Criterium
from competition.serializers import LapSerializer, GroupSerializer, UniversitySerializer, HappyHourSerializer, GroupScoreSerializer

@receiver(post_save, sender=Lap)
def send_lap_update_sse(sender, instance, created, **kwargs):
  if instance.runner.group:
    affected_group = instance.runner.group
    affected_score = GroupScore.objects.get(group=affected_group)
    affected_score.compute()
  
  serializer = LapSerializer(instance)
  send_event('test', 'update_lap', serializer.data)

@receiver(post_delete, sender=Lap)
def send_lap_remove_sse(sender, instance, **kwargs):
  if instance.runner.group:
    affected_group = instance.runner.group
    affected_score = GroupScore.objects.get(group=affected_group)
    affected_score.compute()

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
  try:
    affected_score = GroupScore.objects.get(group=instance)
  except GroupScore.DoesNotExist:
    affected_score = GroupScore(group=instance)
  affected_score.compute()

  serializer = GroupSerializer(instance)
  send_event('test', 'update_group', serializer.data)

@receiver(post_delete, sender=Group)
def send_group_remove_sse(sender, instance, **kwargs):
  serializer = GroupSerializer(instance)
  send_event('test', 'remove_group', serializer.data)

@receiver(post_save, sender=HappyHour)
def send_happyhour_update_sse(sender, instance, created, **kwargs):
  for group_score in GroupScore.objects.all():
    group_score.compute()

  serializer = HappyHourSerializer(instance)
  send_event('test', 'update_happyhour', serializer.data)

@receiver(post_delete, sender=HappyHour)
def send_happyhour_remove_sse(sender, instance, **kwargs):
  for group_score in GroupScore.objects.all():
    group_score.compute()

  serializer = HappyHourSerializer(instance)
  send_event('test', 'remove_happyhour', serializer.data)

@receiver(post_save, sender=Criterium)
def send_happyhour_update_sse(sender, instance, created, **kwargs):
  for group_score in GroupScore.objects.all():
    group_score.compute()

@receiver(post_delete, sender=Criterium)
def send_happyhour_remove_sse(sender, instance, **kwargs):
  for group_score in GroupScore.objects.all():
    group_score.compute()

@receiver(post_save, sender=GroupScore)
def send_group_score_update_sse(sender, instance, created, **kwargs):
  serializer = GroupScoreSerializer(instance)
  send_event('test', 'update_group_score', serializer.data)

@receiver(post_delete, sender=GroupScore)
def send_group_score_remove_sse(sender, instance, **kwargs):
  serializer = GroupScoreSerializer(instance)
  send_event('test', 'remove_group_score', serializer.data)
