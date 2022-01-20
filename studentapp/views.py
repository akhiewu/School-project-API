from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from studentapp.models import Student
from studentapp.serializers import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView


# @csrf_exempt
# def student_list(request):
    
#     if request.method == 'GET':
#         student_var = Student.objects.all()
#         serializer = StudentSerializer(student_var, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    
    
    
# @csrf_exempt
# def student_detail(request, pk):
    
#     try:
#         student_var = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = StudentSerializer(student_var)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(student_var, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         student_var.delete()
#         return HttpResponse(status=204)

 
    #class base api
    
    #-------------------------------------------------------------------
    
    
    
class studentList(APIView):
        
    def get(self, request, format=None):
        student_var = Student.objects.all()
        serializer = StudentSerializer(student_var, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class studentDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student_var = self.get_object(pk)
        serializer = StudentSerializer(student_var)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        student_var = self.get_object(pk)
        serializer = StudentSerializer(student_var, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        student_var = self.get_object(pk)
        student_var.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 