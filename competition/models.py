from django.db import models
from django.core.validators import RegexValidator
import django.utils.timezone as tz
identification_validator = RegexValidator('^[a-zA-Z0-9]{8}$', "This is not a valid university identification number.")

class University(models.Model):
  class Meta:
    verbose_name_plural = 'Universities'
  
  full_name = models.CharField(max_length = 30)
  abbreviation = models.CharField(max_length = 5)
  id_example = models.CharField(max_length = 8)

  def __str__(self):
    return f"{self.full_name} ({self.abbreviation})"

class Runner(models.Model):
  first_name = models.CharField(max_length = 30)
  last_name = models.CharField(max_length = 30)
  identification = models.CharField(
    validators= [
      identification_validator
    ],
    max_length = 8
  )
  university = models.ForeignKey('University', null=True, blank=True, on_delete=models.PROTECT)
  registration_time = models.DateTimeField(auto_now_add = True)
  group = models.ForeignKey('Group', null=True, blank=True, on_delete=models.SET_NULL)

  def __str__(self):
    return f"{self.first_name} {self.last_name} ({self.identification})"

  def save(self, *args, **kwargs):
    self.identification = self.identification.lower()
    return super(Runner, self).save(*args, **kwargs)

class Lap(models.Model):
  runner = models.ForeignKey('Runner', blank=False, on_delete=models.PROTECT)
  registration_time = models.DateTimeField(auto_now_add=True)
  start_time = models.DateTimeField(null=True, blank=True)
  duration = models.IntegerField(null=True, blank=True)

  def __str__(self):
    if self.duration:
      return f"{self.runner.first_name} {self.runner.last_name} ({self.duration/1000}s)"
    else:
      return f"{self.runner.first_name} {self.runner.last_name} (in queue, registered at {self.registration_time})"

class Group(models.Model):
  name = models.CharField(max_length = 30)
  happy_hours = models.ManyToManyField('HappyHour')

  def __str__(self):
    return self.name


class HappyHour(models.Model):
  name = models.CharField(max_length = 20)
  start_time = models.TimeField()
  end_time = models.TimeField()
  multiplier = models.PositiveSmallIntegerField(default = 2)

  def __str__(self):
    return self.name

class Criterium(models.Model):
  upper_limit = models.IntegerField()
  score = models.IntegerField()

  def __str__(self):
    return f"Under {self.upper_limit/1000}s equals {self.score} points"

class GroupScore(models.Model):
  group = models.OneToOneField(Group, on_delete=models.CASCADE)
  score = models.IntegerField(default=0, blank=False)
  
  def compute(self):
    total_points = 0
    local_tz = tz.get_default_timezone()

    members = Runner.objects.filter(group=self.group)
    laps = Lap.objects.filter(runner__in=members)
    for lap in laps:
      lap_points = Criterium.objects.filter(upper_limit__gte=lap.duration).order_by('upper_limit').first().score

      for happy_hour in self.group.happy_hours.all():
        start_time_local = lap.start_time.astimezone(tz=local_tz).time()
        if happy_hour.start_time < start_time_local and happy_hour.end_time > start_time_local:
          lap_points = lap_points*happy_hour.multiplier
          break

      total_points = total_points + lap_points
    self.score = total_points
    self.save()

  def __str__(self):
    return f"Group \'{self.group.name}\': {self.score} points"