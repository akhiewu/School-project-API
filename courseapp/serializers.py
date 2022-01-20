from rest_framework import serializers
from courseapp.models import Course


class CourseSerializer(serializers.Serializer):
   name = serializers.CharField( max_length=30)
   course_code = serializers.CharField( max_length=30)
   
  
   
def create(self, validated_data):
    return Course.objects.create(validated_data)

def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.course_code = validated_data.get('course_code', instance.course_code)
        
        instance.save()
        return instance