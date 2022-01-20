from rest_framework import serializers
from studentapp.models import Student


class StudentSerializer(serializers.Serializer):
    
    name = serializers.CharField( max_length=30)
    cls = serializers.CharField( max_length=30)
    roll = serializers.CharField( max_length=30)
    teacher_select = serializers.CharField( max_length=30)
    
  
   
def create(self, validated_data):
    return Student.objects.create(validated_data)

def update(self, instance, validated_data):
    
        
    instance.name = validated_data.get('name', instance.name)
    instance.cls = validated_data.get('cls', instance.cls)
    instance.roll = validated_data.get('roll', instance.roll)
    instance.teacher_select = validated_data.get('teacher_select', instance.teacher_select)
    instance.save()
    return instance