from django.contrib import admin
from django.contrib.admin import TabularInline

from apps.models import News, User, PhotoGallery, Department, NewsMain, AnnouncementTxt, Announcements, \
    AnnouncementDocuments, AnnouncementEmail, ScientificDevelopments, ScientificDevelopmentsTxt, \
    ScientificDevelopmentsImage, ScientificCouncil, VideoGallery


# Register your models here.


class NewsInline(TabularInline):
    model = NewsMain
    fields = 'txt',
    extra = 1


@admin.register(News)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [NewsInline]


class AnnouncementTxtInline(TabularInline):
    model = AnnouncementTxt
    fields = 'txt',
    extra = 1


class AnnouncementDocumentsInline(TabularInline):
    model = AnnouncementDocuments
    fields = 'documents_txt',
    extra = 1


class AnnouncementEmailInline(TabularInline):
    model = AnnouncementEmail
    fields = 'email',
    extra = 1


@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [AnnouncementTxtInline, AnnouncementDocumentsInline, AnnouncementEmailInline]


class ScientificDevelopmentsTxtInline(TabularInline):
    model = ScientificDevelopmentsTxt
    fields = 'txt',
    extra = 1


class ScientificDevelopmentsIMageInline(TabularInline):
    model = ScientificDevelopmentsImage
    fields = 'image',
    extra = 1


@admin.register(ScientificDevelopments)
class ScientificDevelopmentsAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ScientificDevelopmentsIMageInline, ScientificDevelopmentsTxtInline]


admin.site.register(User)
admin.site.register(ScientificCouncil)
admin.site.register(VideoGallery)
admin.site.register(PhotoGallery)

admin.site.register(Department)
