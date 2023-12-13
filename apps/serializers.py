from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.models import News, User, Department, PhotoGallery, Announcements, \
    AnnouncementEmail, ScientificDevelopments, ScientificDevelopmentsImage, \
    ScientificCouncil, VideoGallery, NewsMainUz, NewsMainRu, NewsMainEng, AnnouncementTxtUz, \
    AnnouncementTxtRu, AnnouncementTxtEng, AnnouncementDocumentsUz, AnnouncementDocumentsRu, AnnouncementDocumentsEng, \
    ScientificDevelopmentsTxtEng, ScientificDevelopmentsTxtRu, ScientificDevelopmentsTxtUz


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'image', 'title_uz', 'title_ru', 'title_eng')


class NewsViewSerializer(ModelSerializer):
    txt_uz = SerializerMethodField()
    txt_ru = SerializerMethodField()
    txt_eng = SerializerMethodField()

    class Meta:
        model = News
        fields = (
            'id', 'image', 'title_uz', 'title_ru', 'title_eng', 'description_uz', 'description_ru', 'description_eng',
            'txt_uz', 'txt_ru', 'txt_eng', 'view', 'created_at')

    def get_txt_uz(self, obj):
        news_main_data = NewsMainUz.objects.filter(
            maintxt_id=obj).values('txt_uz')
        return list(news_main_data)

    def get_txt_ru(self, obj):
        news_main_data = NewsMainRu.objects.filter(
            maintxt_id=obj).values('txt_ru')
        return list(news_main_data)

    def get_txt_eng(self, obj):
        news_main_data = NewsMainEng.objects.filter(
            maintxt_id=obj).values('txt_eng')
        return list(news_main_data)


class UserViewSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'biografiya', 'talim', 'unvon',
                  'kasbiy_faoliyati', 'mukofotlar', 'created_at')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'image', 'full_name', 'yonalish', 'phone_number', 'email', 'ish_vaqti')


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'image', 'full_name', 'yonalish', 'phone_number', 'email', 'xodimlar_soni')


class DepartmentViewSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'full_name', 'bolim_maqsadi')


class AnnouncementsSerializer(ModelSerializer):
    class Meta:
        model = Announcements
        fields = ('id', 'image',)


class AnnouncementsViewSerializer(ModelSerializer):
    txt_uz = SerializerMethodField()
    txt_ru = SerializerMethodField()
    txt_eng = SerializerMethodField()
    documents_txt_uz = SerializerMethodField()
    documents_txt_ru = SerializerMethodField()
    documents_txt_eng = SerializerMethodField()
    email = SerializerMethodField()

    class Meta:
        model = Announcements
        fields = ('id',
                  'image', 'title_uz', 'title_ru', 'title_eng', 'ilmiy_rahbari_uz', 'ilmiy_rahbari_ru',
                  'ilmiy_rahbari_eng', 'ilmiy_rahbari_email',
                  'ilmiy_hamrahbari_uz', 'ilmiy_hamrahbari_ru', 'ilmiy_hamrahbari_eng',
                  'ilmiy_hamrahbari_email',
                  'txt_uz', 'txt_ru', 'txt_eng', 'documents_txt_uz', 'documents_txt_ru', 'documents_txt_eng', 'email')

    def get_txt_uz(self, obj):
        news_main_data = AnnouncementTxtUz.objects.filter(
            maintxt_id=obj).values('txt_uz')
        return list(news_main_data)

    def get_txt_ru(self, obj):
        news_main_data = AnnouncementTxtRu.objects.filter(
            maintxt_id=obj).values('txt_ru')
        return list(news_main_data)

    def get_txt_eng(self, obj):
        news_main_data = AnnouncementTxtEng.objects.filter(
            maintxt_id=obj).values('txt_eng')
        return list(news_main_data)

    def get_documents_txt_uz(self, obj):
        news_main_data = AnnouncementDocumentsUz.objects.filter(
            documents_id=obj).values('documents_txt_uz')
        return list(news_main_data)

    def get_documents_txt_ru(self, obj):
        news_main_data = AnnouncementDocumentsRu.objects.filter(
            documents_id=obj).values('documents_txt_ru')
        return list(news_main_data)

    def get_documents_txt_eng(self, obj):
        news_main_data = AnnouncementDocumentsEng.objects.filter(
            documents_id=obj).values('documents_txt_eng')
        return list(news_main_data)

    def get_email(self, obj):
        news_main_data = AnnouncementEmail.objects.filter(
            emails_id=obj).values('email')
        return list(news_main_data)


class ScientificDevelopmentsSerializer(ModelSerializer):
    class Meta:
        model = ScientificDevelopments
        fields = ('id', 'title',)


class ScientificDevelopmentsViewSerializer(ModelSerializer):
    txt_uz = SerializerMethodField()
    txt_ru = SerializerMethodField()
    txt_eng = SerializerMethodField()
    image = SerializerMethodField()

    class Meta:
        model = ScientificDevelopments
        fields = ('id', 'title_uz', 'title_ru', 'title_eng', 'image', 'txt_uz', 'txt_ru', 'txt_eng')

    def get_image(self, obj):
        news_main_data = ScientificDevelopmentsImage.objects.filter(
            developments_id=obj).values('image')
        return list(news_main_data)

    def get_txt_uz(self, obj):
        news_main_data = ScientificDevelopmentsTxtUz.objects.filter(
            developments_id=obj).values('txt_uz')
        return list(news_main_data)

    def get_txt_ru(self, obj):
        news_main_data = ScientificDevelopmentsTxtRu.objects.filter(
            developments_id=obj).values('txt_ru')
        return list(news_main_data)

    def get_txt_eng(self, obj):
        news_main_data = ScientificDevelopmentsTxtEng.objects.filter(
            developments_id=obj).values('txt_eng')
        return list(news_main_data)


class ScientificCouncilSerializer(ModelSerializer):
    class Meta:
        model = ScientificCouncil
        fields = ('id', 'fish_uz','fish_ru','fish_eng', 'ish_uz','ish_ru','ish_eng', 'academic_degree_uz','academic_degree_ru','academic_degree_eng')


class VideoGallerySerializer(ModelSerializer):
    # url = SerializerMethodField()
    class Meta:
        model = VideoGallery
        fields = '__all__'


class PhotoGallerySerializer(ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = ('id', 'image',)


class PhotoGalleryViewSerializer(ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = ('id', 'image', 'created_at')
