from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from education.models import Product, Lesson, Group
from education.permisions import IsOwner
from education.serializers import ProductSerializer, LessonSerializer, GroupSerializer


# Create your views here.


class ProductCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()


class ProductView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsOwner]
    queryset = Product.objects.all()


class LessonCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()


class LessonView(RetrieveUpdateDestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]
    queryset = Lesson.objects.all()


class GroupCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    queryset = Group.objects.all()


class GroupView(RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsOwner]
    queryset = Group.objects.all()


# class ProductListAPIView(generics.ListAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()



# class ProductUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#
#
# class ProductDestroyAPIView(generics.DestroyAPIView):
#     queryset = Product.objects.all()

