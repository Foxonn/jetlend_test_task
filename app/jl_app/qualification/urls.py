from django.urls import path

from . import views
urlpatterns = [
    path('passport/', views.AddPassportView.as_view()),
    path('passport_image/', views.AddImagePassportView.as_view()),
    path('document/', views.AddQualificationDocsView.as_view()),
    path('status/', views.QualificationStatusView.as_view()),
    path('confirm/', views.ConfirmRulesView.as_view()),
    path('', views.QualificationInit.as_view()),
]

