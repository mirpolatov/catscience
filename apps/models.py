from django.db import models
from django.db.models import CASCADE


# Create your models here.


class News(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    # maintxt = models.TextField()
    view = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class NewsMain(models.Model):
    maintxt = models.ForeignKey(News, on_delete=CASCADE, related_name='news')
    txt = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    image = models.ImageField(upload_to='images/')
    full_name = models.CharField(max_length=255)
    yonalish = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    ish_vaqti = models.CharField(max_length=255)
    biografiya = models.CharField(max_length=255)
    talim = models.CharField(max_length=255)
    unvon = models.CharField(max_length=100)
    kasbiy_faoliyati = models.CharField(max_length=400)
    mukofotlar = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Department(models.Model):
    image = models.ImageField(upload_to='images/')
    full_name = models.CharField(max_length=255)
    yonalish = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    xodimlar_soni = models.IntegerField()
    bolim_maqsadi = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class PhotoGallery(models.Model):
    image = models.ImageField(upload_to='images/gallery')
    created_at = models.DateTimeField(auto_now_add=True)


class Announcements(models.Model):
    image = models.ImageField(upload_to='images/announcements')
    title = models.CharField(max_length=255)
    ilmiy_rahbari = models.CharField(max_length=50)
    ilmiy_rahbari_email = models.EmailField()
    ilmiy_hamrahbari = models.CharField(max_length=50)
    ilmiy_hamrahbari_email = models.EmailField()


class AnnouncementTxt(models.Model):
    maintxt = models.ForeignKey(Announcements, on_delete=CASCADE, related_name='announcements')
    txt = models.TextField()


class AnnouncementDocuments(models.Model):
    documents = models.ForeignKey(Announcements, on_delete=CASCADE, related_name='announcements_documents')
    documents_txt = models.TextField()


class AnnouncementEmail(models.Model):
    emails = models.ForeignKey(Announcements, on_delete=CASCADE, related_name='announcements_email')
    email = models.EmailField()


class ScientificDevelopments(models.Model):
    title = models.CharField(max_length=500)


class ScientificDevelopmentsImage(models.Model):
    developments = models.ForeignKey(ScientificDevelopments, on_delete=CASCADE, related_name='developments_image')
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class ScientificDevelopmentsTxt(models.Model):
    developments = models.ForeignKey(ScientificDevelopments, on_delete=CASCADE, related_name='developments_txt')
    txt = models.TextField()


class ScientificCouncil(models.Model):
    fish = models.CharField(max_length=100)
    ish = models.CharField(max_length=255, null=True, blank=True)
    academic_degree = models.CharField(max_length=255)


class VideoGallery(models.Model):
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
