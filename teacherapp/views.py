from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from teacherapp.models import Teacher
from teacherapp.serializers import TeacherSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView




#----------------------------------------------------------------
# @csrf_exempt
# def teacher_list(request):
    
#     if request.method == 'GET':
#         teacher_var = Teacher.objects.all()
#         serializer = TeacherSerializer(teacher_var, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = TeacherSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
    
    
    
# @csrf_exempt
# def teacher_detail(request, pk):
    
#     try:
#         teacher_var = Teacher.objects.get(pk=pk)
#     except Teacher.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = TeacherSerializer(teacher_var)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = TeacherSerializer(teacher_var, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         teacher_var.delete()
#         return HttpResponse(status=204)



#Funtion Base API
#---------------------------------------------------------------------

# @api_view(['GET', 'POST'])
# def teacher_list(request):
   
#     if request.method == 'GET':
#         teacher_var = Teacher.objects.all()
#         serializer = TeacherSerializer(teacher_var, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TeacherSerializer(data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# @api_view(['GET', 'PUT', 'DELETE'])
# def teacher_detail(request, pk):
    
#     try:
#         teacher_var = Teacher.objects.get(pk=pk)
#     except Teacher.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = TeacherSerializer(teacher_var)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = TeacherSerializer(teacher_var, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         teacher_var.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    
    
    
    
    
    
    #class base api
    
    #-------------------------------------------------------------------
    
    
class teacherList(APIView):
        
    def get(self, request, format=None):
        teacher_var = Teacher.objects.all()
        serializer = TeacherSerializer(teacher_var, many=True)
        return Response(serializer.data)

    def Post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class teacherDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        teacher_var = self.get_object(pk)
        serializer = TeacherSerializer(teacher_var)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        teacher_var = self.get_object(pk)
        serializer = TeacherSerializer(teacher_var, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        teacher_var = self.get_object(pk)
        teacher_var.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    