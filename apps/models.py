from django.db import models
from django.db.models import CASCADE


# Create your models here.


class News(models.Model):
    image = models.ImageField(upload_to='images/')
    title_uz = models.CharField(max_length=255, null=True, blank=True)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_eng = models.CharField(max_length=255, null=True, blank=True)
    description_uz = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_eng = models.TextField(null=True, blank=True)
    view = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class NewsMainUz(models.Model):
    maintxt = models.ForeignKey(News, on_delete=CASCADE, related_name='news_uz')
    txt_uz = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


class NewsMainRu(models.Model):
    maintxt = models.ForeignKey(News, on_delete=CASCADE, related_name='news_ru')
    txt_ru = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


class NewsMainEng(models.Model):
    maintxt = models.ForeignKey(News, on_delete=CASCADE, related_name='news_eng')
    txt_eng = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    image = models.ImageField(upload_to='images/')
    full_name_uz = models.CharField(max_length=255, null=True, blank=True)
    full_name_ru = models.CharField(max_length=255, null=True, blank=True)
    full_name_eng = models.CharField(max_length=255, null=True, blank=True)
    yonalish_uz = models.CharField(max_length=255, null=True, blank=True)
    yonalish_ru = models.CharField(max_length=255, null=True, blank=True)
    yonalish_eng = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    ish_vaqti_uz = models.CharField(max_length=255, null=True, blank=True)
    ish_vaqti_ru = models.CharField(max_length=255, null=True, blank=True)
    ish_vaqti_eng = models.CharField(max_length=255, null=True, blank=True)
    biografiya_uz = models.CharField(max_length=255, null=True, blank=True)
    biografiya_ru = models.CharField(max_length=255, null=True, blank=True)
    biografiya_eng = models.CharField(max_length=255, null=True, blank=True)
    talim_uz = models.CharField(max_length=255, null=True, blank=True)
    talim_ru = models.CharField(max_length=255, null=True, blank=True)
    talim_eng = models.CharField(max_length=255, null=True, blank=True)
    unvon_uz = models.CharField(max_length=100, null=True, blank=True)
    unvon_ru = models.CharField(max_length=100, null=True, blank=True)
    unvon_eng = models.CharField(max_length=100, null=True, blank=True)
    kasbiy_faoliyati_uz = models.CharField(max_length=400, null=True, blank=True)
    kasbiy_faoliyati_ru = models.CharField(max_length=400, null=True, blank=True)
    kasbiy_faoliyati_eng = models.CharField(max_length=400, null=True, blank=True)
    mukofotlar_uz = models.CharField(max_length=255, null=True, blank=True)
    mukofotlar_ru = models.CharField(max_length=255, null=True, blank=True)
    mukofotlar_eng = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Department(models.Model):
    image = models.ImageField(upload_to='images/')
    full_name_uz = models.CharField(max_length=255, null=True, blank=True)
    full_name_ru = models.CharField(max_length=255, null=True, blank=True)
    full_name_eng = models.CharField(max_length=255, null=True, blank=True)
    yonalish_uz = models.CharField(max_length=255, null=True, blank=True)
    yonalish_ru = models.CharField(max_length=255, null=True, blank=True)
    yonalish_eng = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    xodimlar_soni = models.IntegerField()
    bolim_maqsadi_uz = models.TextField(null=True, blank=True)
    bolim_maqsadi_ru = models.TextField(null=True, blank=True)
    bolim_maqsadi_eng = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PhotoGallery(models.Model):
    image = models.ImageField(upload_to='images/gallery')
    created_at = models.DateTimeField(auto_now_add=True)


class Announcements(models.Model):
    image = models.ImageField(upload_to='images/announcements')
    title_uz = models.CharField(max_length=255, null=True, blank=True)
    title_ru = models.CharField(max_length=255, null=True, blank=True)
    title_eng = models.CharField(max_length=255, null=True, blank=True)
    ilmiy_rahbari_uz = models.CharField(max_length=50, null=True, blank=True)
    ilmiy_rahbari_ru = models.CharField(max_length=50, null=True, blank=True)
    ilmiy_rahbari_eng = models.CharField(max_length=50, null=True, blank=True)
    ilmiy_rahbari_email = models.EmailField()
    ilmiy_hamrahbari_uz = models.CharField(max_length=50, null=True, blank=True)
    ilmiy_hamrahbari_ru = models.CharField(max_length=50, null=True, blank=True)
    ilmiy_hamrahbari_eng = models.CharField(max_length=50, null=True, blank=True)
    ilmiy_hamrahbari_email = models.EmailField()


class AnnouncementTxtUz(models.Model):
    maintxt = models.ForeignKey(Announcements, on_delete=CASCADE, related_name='announcements_uz')
    txt_uz = models.TextField(null=True, blank=True)


class AnnouncementTxtRu(models.Model):
    maintxt = models.ForeignKey(Announcements, on_delete=CASCADE, related_name='announcements_ru')
    txt_ru = models.TextField(null=True, blank=True)


class AnnouncementTxtEng(models.Model):
    maintxt = models.ForeignKey(Announcements, on_delete=CASCADE, related_name='announcements_eng')
    txt_eng = models.TextField(null=True, blank=True)


class AnnouncementDocumentsUz(models.Model):
    documents = models.ForeignKey(Announcements, on_delete=CASCADE, related_name='announcements_documents_uz')
    documents_txt_uz = models.TextField(null=True, blank=True)


class AnnouncementDocumentsRu(models.Model):
    documents = models.ForeignKey(Announcements, on_delete=CASCADE, related_name='announcements_documents_ru')
    documents_txt_ru = models.TextField(null=True, blank=True)


class AnnouncementDocumentsEng(models.Model):
    documents = models.ForeignKey(Announcements, on_delete=CASCADE, related_name='announcements_documents_eng')
    documents_txt_eng = models.TextField(null=True, blank=True)


class AnnouncementEmail(models.Model):
    emails = models.ForeignKey(Announcements, on_delete=CASCADE, related_name='announcements_email')
    email = models.EmailField()


class ScientificDevelopments(models.Model):
    title_uz = models.CharField(max_length=500, null=True, blank=True)
    title_ru = models.CharField(max_length=500, null=True, blank=True)
    title_eng = models.CharField(max_length=500, null=True, blank=True)


class ScientificDevelopmentsImage(models.Model):
    developments = models.ForeignKey(ScientificDevelopments, on_delete=CASCADE, related_name='developments_image')
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class ScientificDevelopmentsTxtUz(models.Model):
    developments = models.ForeignKey(ScientificDevelopments, on_delete=CASCADE, related_name='developments_txt_uz')
    txt_uz = models.TextField(null=True, blank=True)


class ScientificDevelopmentsTxtRu(models.Model):
    developments = models.ForeignKey(ScientificDevelopments, on_delete=CASCADE, related_name='developments_txt_ru')
    txt_ru = models.TextField(null=True, blank=True)


class ScientificDevelopmentsTxtEng(models.Model):
    developments = models.ForeignKey(ScientificDevelopments, on_delete=CASCADE, related_name='developments_txt_eng')
    txt_eng = models.TextField(null=True, blank=True)


class ScientificCouncil(models.Model):
    fish_uz = models.CharField(max_length=100, null=True, blank=True)
    fish_ru = models.CharField(max_length=100, null=True, blank=True)
    fish_eng = models.CharField(max_length=100, null=True, blank=True)
    ish_uz = models.CharField(max_length=255, null=True, blank=True)
    ish_ru = models.CharField(max_length=255, null=True, blank=True)
    ish_eng = models.CharField(max_length=255, null=True, blank=True)
    academic_degree_uz = models.CharField(max_length=255, null=True, blank=True)
    academic_degree_ru = models.CharField(max_length=255, null=True, blank=True)
    academic_degree_eng = models.CharField(max_length=255, null=True, blank=True)


class VideoGallery(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
