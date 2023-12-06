from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.models import News, User, Department, Announcements, ScientificDevelopments, ScientificCouncil, VideoGallery, \
    PhotoGallery
from apps.serializers import NewsSerializer, NewsViewSerializer, UserViewSerializer, UserSerializer, \
    DepartmentSerializer, DepartmentViewSerializer, AnnouncementsSerializer, AnnouncementsViewSerializer, \
    ScientificDevelopmentsSerializer, ScientificDevelopmentsViewSerializer, ScientificCouncilSerializer, \
    VideoGallerySerializer, PhotoGallerySerializer, PhotoGalleryViewSerializer


# Create your views here.

class NewsModelView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class NewsIdView(RetrieveModelMixin, GenericAPIView):
    queryset = News.objects.all()
    serializer_class = NewsViewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserModelView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserIdView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            serializer = UserViewSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"errors": "User not found"}, status=404)


class DepartmentModelView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DepartmentIdView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        try:
            department = Department.objects.get(id=id)
            serializer = DepartmentViewSerializer(department)
            return Response(serializer.data)
        except Department.DoesNotExist:
            return Response({"errors": "Department not found"}, status=404)


class AnnouncementsModelView(ListAPIView):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AnnouncementsIdView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        try:
            department = Announcements.objects.get(id=id)
            serializer = AnnouncementsViewSerializer(department)
            return Response(serializer.data)
        except Announcements.DoesNotExist:
            return Response({"errors": "Announcements not found"}, status=404)


class ScientificDevelopmentsModelView(ListAPIView):
    queryset = ScientificDevelopments.objects.all()
    serializer_class = ScientificDevelopmentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ScientificDevelopmentsIdView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        try:
            department = ScientificDevelopments.objects.get(id=id)
            serializer = ScientificDevelopmentsViewSerializer(department)
            return Response(serializer.data)
        except ScientificDevelopments.DoesNotExist:
            return Response({"errors": "Scientific Developments not found"}, status=404)


class ScientificCouncilModelView(ListAPIView):
    queryset = ScientificCouncil.objects.all()
    serializer_class = ScientificCouncilSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class VideoGalleryModelView(ListAPIView):
    queryset = VideoGallery.objects.all()
    serializer_class = VideoGallerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     return VideoGallery.objects.all()

    # def get_queryset(self):
    #     # s = []
    #     queryset = VideoGallery.objects.all()
    #     for video_gallery in enumerate(queryset):
    #         values_list = list(video_gallery)
    #         return values_list


class PhotoGalleryModelView(ListAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PhotoGalleryIdView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        try:
            department = PhotoGallery.objects.get(id=id)
            serializer = PhotoGalleryViewSerializer(department)
            return Response(serializer.data)
        except PhotoGallery.DoesNotExist:
            return Response({"errors": "Image  not found"}, status=404)
