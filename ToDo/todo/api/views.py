from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken

from knox.auth import TokenAuthentication

from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.models import User
from django.views.generic import ListView
#from .models import CrudUser
from django.http import JsonResponse
from rest_framework.views import APIView

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


   
# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
 
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
        

#list users
class UserApi(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request,id=None):
       
        if id:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
 
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  

  

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

        
    def put(self, request, id=None):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
 
 
    def delete(self, request, id=None):
        user = get_object_or_404(User, id=id)
        user.delete()
        return Response({"status": "success", "data": "user Deleted"})
   
    
     
class UserRandomApi(APIView):
        
        permission_classes = (permissions.AllowAny,)
         
       #get random records
        def get( self, request):
            from random import choice
            pks = User.objects.values_list('pk', flat=True)
            random_pk = choice(pks)
            random_obj = User.objects.get(pk=random_pk)
    
          
            serializer = UserSerializer(random_obj)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  

            


           