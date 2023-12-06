from collections import OrderedDict
from typing import OrderedDict
from collections import OrderedDict
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SkipField, ListField, SerializerMethodField
from rest_framework.relations import PKOnlyObject
from rest_framework.serializers import ModelSerializer

from apps.models import News, User, Department, PhotoGallery, NewsMain, Announcements, AnnouncementTxt, \
    AnnouncementDocuments, AnnouncementEmail, ScientificDevelopments, ScientificDevelopmentsImage, \
    ScientificDevelopmentsTxt, ScientificCouncil, VideoGallery


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('image', 'title')


class NewsViewSerializer(ModelSerializer):
    txt = SerializerMethodField()

    class Meta:
        model = News
        fields = ('image', 'title', 'description', 'txt', 'view', 'created_at')

    def get_txt(self, obj):
        news_main_data = NewsMain.objects.filter(
            maintxt_id=obj).values('txt')
        return list(news_main_data)


class UserViewSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'biografiya', 'talim', 'unvon',
            'kasbiy_faoliyati', 'mukofotlar', 'created_at')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'image', 'full_name', 'yonalish', 'phone_number', 'email', 'ish_vaqti')


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('image', 'full_name', 'yonalish', 'phone_number', 'email', 'xodimlar_soni')


class DepartmentViewSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('full_name', 'bolim_maqsadi')


class AnnouncementsSerializer(ModelSerializer):
    class Meta:
        model = Announcements
        fields = ('image',)


class AnnouncementsViewSerializer(ModelSerializer):
    txt = SerializerMethodField()
    documents_txt = SerializerMethodField()
    email = SerializerMethodField()

    class Meta:
        model = Announcements
        fields = (
            'image', 'title', 'ilmiy_rahbari', 'ilmiy_rahbari_email', 'ilmiy_hamrahbari', 'ilmiy_hamrahbari_email',
            'txt', 'documents_txt', 'email')

    def get_txt(self, obj):
        news_main_data = AnnouncementTxt.objects.filter(
            maintxt_id=obj).values('txt')
        return list(news_main_data)

    def get_documents_txt(self, obj):
        news_main_data = AnnouncementDocuments.objects.filter(
            documents_id=obj).values('documents_txt')
        return list(news_main_data)

    def get_email(self, obj):
        news_main_data = AnnouncementEmail.objects.filter(
            emails_id=obj).values('email')
        return list(news_main_data)


class ScientificDevelopmentsSerializer(ModelSerializer):
    class Meta:
        model = ScientificDevelopments
        fields = ('title',)


class ScientificDevelopmentsViewSerializer(ModelSerializer):
    txt = SerializerMethodField()
    image = SerializerMethodField()

    class Meta:
        model = ScientificDevelopments
        fields = ('title', 'image', 'txt')

    def get_image(self, obj):
        news_main_data = ScientificDevelopmentsImage.objects.filter(
            developments_id=obj).values('image')
        return list(news_main_data)

    def get_txt(self, obj):
        news_main_data = ScientificDevelopmentsTxt.objects.filter(
            developments_id=obj).values('txt')
        return list(news_main_data)


class ScientificCouncilSerializer(ModelSerializer):
    class Meta:
        model = ScientificCouncil
        fields = ('fish', 'ish', 'academic_degree')


class VideoGallerySerializer(ModelSerializer):
    # url = SerializerMethodField()

    class Meta:
        model = VideoGallery
        fields = '__all__'


class PhotoGallerySerializer(ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = ('image',)


class PhotoGalleryViewSerializer(ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = ('id', 'image', 'created_at')
