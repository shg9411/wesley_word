from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('word/',views.WordLV.as_view(), name='words'),
    path('word/new/',views.WordCV.as_view(), name='word-new'),
    path('word/<int:pk>/',views.WordDV.as_view(), name='word-detail'),
    path('word/<int:pk>/delete/',views.WordDelV.as_view(),name='word-delete'),
    path('word/<int:pk>/edit/',views.WordUV.as_view(),name='word-edit'),
    path('search/',views.search.as_view(), name='search'),
    path('wordbook/<int:pk>/',views.detail,name='detail'),
    path('getNextVerb/',views.getNextVerb),
    path('getNextSub/',views.getNextSub),
    path('getNextObj/',views.getNextObj),
    path('getPrevVerb/',views.getPrevVerb),
    path('getPrevSub/',views.getPrevSub),
    path('getPrevObj/',views.getPrevObj),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
