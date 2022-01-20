from rest_framework import serializers
from clsapp.models import Cls


class ClsSerializer(serializers.Serializer):
   name = serializers.CharField( max_length=30)
   section = serializers.CharField( max_length=30)
   
  
   
def create(self, validated_data):
    return Cls.objects.create(validated_data)

def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.section = validated_data.get('section', instance.section)
        
        instance.save()
        return instance