from rest_framework import serializers
from .models import Runner, Lap, Group, HappyHour, University

class UniversitySerializer(serializers.ModelSerializer):
  class Meta:
    model = University
    fields = '__all__'

class RunnerSerializer(serializers.ModelSerializer):
  def to_representation(self, instance):
    self.fields['group'] = GroupSerializer(read_only=True)
    return super(RunnerSerializer, self).to_representation(instance)

  class Meta:
    model = Runner
    fields = '__all__'

class LapSerializer(serializers.ModelSerializer):
  class Meta:
    model = Lap
    fields = '__all__'

  def to_representation(self, instance):
    self.fields['runner'] = RunnerSerializer(read_only=True)
    return super(LapSerializer, self).to_representation(instance)

class GroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = Group
    fields = '__all__'

  def to_representation(self, instance):
    self.fields['happy_hours'] = HappyHourSerializer(many=True, read_only=True)
    return super(GroupSerializer, self).to_representation(instance)

class HappyHourSerializer(serializers.ModelSerializer):
  class Meta:
    model = HappyHour
    fields = '__all__'

# class DepartmentSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Department
#     fields = '__all__'