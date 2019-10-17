from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Runner, Lap, Group, HappyHour, University
from .serializers import RunnerSerializer, LapSerializer, GroupSerializer, HappyHourSerializer, UniversitySerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
import datetime

class RunnerViewSet(viewsets.ModelViewSet):
  queryset = Runner.objects.all()
  serializer_class = RunnerSerializer
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
  ordering_fields = ['first_name', 'last_name', 'identification']
  filterset_fields = ['first_name', 'last_name', 'identification']

class LapViewSet(viewsets.ModelViewSet):
  queryset = Lap.objects.all()
  serializer_class = LapSerializer
  filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
  ordering_fields = ['start_time', 'duration', 'registration_time', 'runner']
  filterset_fields = ['start_time', 'duration', 'registration_time', 'runner']

  @action(detail=False, methods=['post'])
  def advance(self, request):
    try:
      current_lap = Lap.objects.get(start_time__isnull=False, duration__isnull=True)
      current_lap.duration = (datetime.datetime.now(datetime.timezone.utc) - current_lap.start_time).total_seconds()*1000
      current_lap.save()
    except MultipleObjectsReturned as e:
      return Response({'message': "Multiple laps exist which could be currently active."}, status_code=500)
    except ObjectDoesNotExist as e:
      print('No lap is currently active')

    new_lap = Lap.objects.filter(start_time__isnull=True, duration__isnull=True).order_by('registration_time').first()

    if new_lap is not None:
      new_lap.start_time = datetime.datetime.now(datetime.timezone.utc)
      new_lap.save()
    else:
      print("No lap is available in the queue.")
    return Response({'message': "Started the next lap."})

  @action(detail=False, methods=['post'])
  def reverse(self, request):
    try:
      current_lap = Lap.objects.get(start_time__isnull=False, duration__isnull=True)
      current_lap.start_time = None
      current_lap.save()
    except MultipleObjectsReturned as e:
      return Response({'message': "Multiple laps exist which could be currently active."}, status_code=500)
    except ObjectDoesNotExist as e:
      print('No lap is currently active')

    previous_lap = Lap.objects.filter(start_time__isnull=False, duration__isnull=False).order_by('-registration_time').first()

    if previous_lap is not None:
      previous_lap.duration = None
      previous_lap.save()
    else:
      print("No finished laps were found.")
    return Response({'message': "Started the next lap."})

class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  filter_backends = [filters.OrderingFilter]
  ordering_fields = ['name']

class HappyHourViewSet(viewsets.ModelViewSet):
  queryset = HappyHour.objects.all()
  serializer_class = HappyHourSerializer

# class DepartmentViewSet(viewsets.ModelViewSet):
#   queryset = Department.objects.all()
#   serializer_class = DepartmentSerializer

class UniversityViewSet(viewsets.ModelViewSet):
  queryset = University.objects.all()
  serializer_class = UniversitySerializer