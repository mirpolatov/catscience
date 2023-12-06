from django.urls import path

from apps.views import NewsModelView, NewsIdView, UserModelView, UserIdView, DepartmentModelView, DepartmentIdView, \
    AnnouncementsModelView, AnnouncementsIdView, ScientificDevelopmentsModelView, ScientificDevelopmentsIdView, \
    ScientificCouncilModelView, VideoGalleryModelView, PhotoGalleryModelView, PhotoGalleryIdView

urlpatterns = [
    path('news-list/', NewsModelView.as_view()),
    path('news/view_id/<int:pk>/', NewsIdView.as_view()),
    path('user-list/', UserModelView.as_view()),
    path('user/view_id/<int:id>/', UserIdView.as_view()),
    path('department-list/', DepartmentModelView.as_view()),
    path('department/view_id/<int:id>/', DepartmentIdView.as_view()),
    path('announcements-list/', AnnouncementsModelView.as_view()),
    path('announcements/view_id/<int:id>/', AnnouncementsIdView.as_view()),
    path('ScientificDevelopments-list/', ScientificDevelopmentsModelView.as_view()),
    path('ScientificDevelopments/view_id/<int:id>/', ScientificDevelopmentsIdView.as_view()),
    path('ScientificCouncil-list/', ScientificCouncilModelView.as_view()),
    path('VideoGallery-list/', VideoGalleryModelView.as_view()),
    path('PhotoGallery-list/', PhotoGalleryModelView.as_view()),
    path('PhotoGallery/view_id/<int:id>/', PhotoGalleryIdView.as_view()),

]
