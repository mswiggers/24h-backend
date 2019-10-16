from django.db import models
from django.core.validators import RegexValidator
identification_validator = RegexValidator('^[a-zA-Z0-9]{0,8}$', "This is not a valid university identification number.")

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
  group = models.ForeignKey('Group', null=True, blank=True, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.first_name} {self.last_name} ({self.identification})"

  def save(self, *args, **kwargs):
    self.identification = self.identification.lower()
    return super(Runner, self).save(*args, **kwargs)

class Lap(models.Model):
  runner = models.ForeignKey('Runner', on_delete=models.PROTECT)
  registration_time = models.DateTimeField(auto_now_add=True)
  start_time = models.DateTimeField(null=True, blank=True)
  duration = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return f"{self.runner.first_name} {self.runner.last_name} {self.registration_time}"

class Group(models.Model):
  name = models.CharField(max_length = 30)
  happy_hours = models.ManyToManyField('HappyHour')

  def __str__(self):
    return self.name

class HappyHour(models.Model):
  name = models.CharField(max_length = 20)
  start_time = models.TimeField()
  end_time = models.TimeField()
  bonus = models.PositiveSmallIntegerField(default = 2)

  def __str__(self):
    return self.name

# class Department(models.Model):
#   name = models.CharField(max_length = 50)
#   abbreviation = models.CharField(max_length = 5)

#   def __str__(self):
#     return self.name

class LapTime(models.Model):
  upper_limit = models.DurationField()
  score = models.IntegerField()
