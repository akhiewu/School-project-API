from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.Serializer):
    
    
    name = serializers.CharField( max_length=30)
    department = serializers.CharField( max_length=30)
    designation = serializers.CharField( max_length=30)
    course_code = serializers.CharField(max_length=20)
   
    def create(self, validated_data):
        return Teacher.objects.create(validated_data)
    

    

    def update(self, instance, validated_data):
            
        instance.name = validated_data.get('name', instance.name)
        instance.department = validated_data.get('department', instance.department)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.course_code = validated_data.get('course_code', instance.course_code)
        instance.save()
        return instance
      
      
      
      
      # class TeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         fields = ['name', 'department', 'designation', 'course_code']