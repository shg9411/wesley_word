from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('word/',views.WordLV.as_view(), name='words'),
    path('search/',views.search.as_view(), name='search'),
    path('wordbook/<int:pk>/',views.detail,name='detail'),
    path('getNextVerb/',views.getNextVerb),
    path('getNextSub/',views.getNextSub),
    path('getNextObj/',views.getNextObj),
    path('getPrevVerb/',views.getPrevVerb),
    path('getPrevSub/',views.getPrevSub),
    path('getPrevObj/',views.getPrevObj),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
