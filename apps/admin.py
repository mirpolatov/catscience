from django.contrib import admin
from django.contrib.admin import TabularInline

from apps.models import News, User, PhotoGallery, Department, AnnouncementTxtUz, Announcements, \
    AnnouncementEmail, ScientificDevelopments, \
    ScientificDevelopmentsImage, ScientificCouncil, VideoGallery, NewsMainUz, NewsMainRu, NewsMainEng, \
    AnnouncementTxtRu, AnnouncementTxtEng, AnnouncementDocumentsUz, AnnouncementDocumentsRu, AnnouncementDocumentsEng, \
    ScientificDevelopmentsTxtUz, ScientificDevelopmentsTxtRu, ScientificDevelopmentsTxtEng


# Register your models here.


class NewsUZInline(TabularInline):
    model = NewsMainUz
    fields = 'txt_uz',
    extra = 1


class NewsRuInline(TabularInline):
    model = NewsMainRu
    fields = 'txt_ru',
    extra = 1


class NewsEngInline(TabularInline):
    model = NewsMainEng
    fields = 'txt_eng',
    extra = 1


@admin.register(News)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'title_ru', 'title_eng']
    inlines = [NewsUZInline, NewsRuInline, NewsEngInline]


class AnnouncementTxtInlineUz(TabularInline):
    model = AnnouncementTxtUz
    fields = 'txt_uz',
    extra = 1


class AnnouncementTxtInlineRu(TabularInline):
    model = AnnouncementTxtRu
    fields = 'txt_ru',
    extra = 1


class AnnouncementTxtInlineEng(TabularInline):
    model = AnnouncementTxtEng
    fields = 'txt_eng',
    extra = 1


class AnnouncementDocumentsInlineUz(TabularInline):
    model = AnnouncementDocumentsUz
    fields = 'documents_txt_uz',
    extra = 1


class AnnouncementDocumentsInlineRu(TabularInline):
    model = AnnouncementDocumentsRu
    fields = 'documents_txt_ru',
    extra = 1


class AnnouncementDocumentsInlineEng(TabularInline):
    model = AnnouncementDocumentsEng
    fields = 'documents_txt_eng',
    extra = 1


class AnnouncementEmailInline(TabularInline):
    model = AnnouncementEmail
    fields = 'email',
    extra = 1


@admin.register(Announcements)
class AnnouncementsAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'title_ru', 'title_eng']
    inlines = [AnnouncementEmailInline, AnnouncementDocumentsInlineUz, AnnouncementDocumentsInlineRu,
               AnnouncementDocumentsInlineEng, AnnouncementTxtInlineEng, AnnouncementTxtInlineRu,
               AnnouncementTxtInlineUz]


class ScientificDevelopmentsTxtInlineUz(TabularInline):
    model = ScientificDevelopmentsTxtUz
    fields = 'txt_uz',
    extra = 1


class ScientificDevelopmentsTxtInlineRu(TabularInline):
    model = ScientificDevelopmentsTxtRu
    fields = 'txt_ru',
    extra = 1


class ScientificDevelopmentsTxtInlineEng(TabularInline):
    model = ScientificDevelopmentsTxtEng
    fields = 'txt_eng',
    extra = 1


class ScientificDevelopmentsIMageInline(TabularInline):
    model = ScientificDevelopmentsImage
    fields = 'image',
    extra = 1


@admin.register(ScientificDevelopments)
class ScientificDevelopmentsAdmin(admin.ModelAdmin):
    list_display = ['title_uz', 'title_ru', 'title_eng']
    inlines = [ScientificDevelopmentsIMageInline, ScientificDevelopmentsTxtInlineUz, ScientificDevelopmentsTxtInlineRu,
               ScientificDevelopmentsTxtInlineEng]


admin.site.register(User)
admin.site.register(ScientificCouncil)
admin.site.register(VideoGallery)
admin.site.register(PhotoGallery)

admin.site.register(Department)
