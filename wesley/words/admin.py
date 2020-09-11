from django.contrib import admin
from . import models
from django.db.models.functions import Lower

@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.zoom)
class ZoomAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['zoom']
    pass

@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display=['word','mean']
    list_filter = ('word_type',)
    search_fields = ['word']

    def get_ordering(self,request):
        return [Lower('word')]

@admin.register(models.WordBook)
class WordBookAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['teacher','_class','title']
    search_fields = ['title']
    ordering = ('title',)

    fieldsets = [
        ('Title', {'fields':['teacher','_class','title']}),
        ('List',{'fields':['subjects','verbs','objs']}),
    ]

@admin.register(models.sList)
class sListAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['word_count']
    filter_horizontal = ["subject"]

    def word_count(self,obj):
        return models.Word.objects.filter(slist=obj).count()

@admin.register(models.vList)
class vListAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['word_count']
    filter_horizontal = ["verb"]

    def word_count(self,obj):
        return models.Word.objects.filter(vlist=obj).count()

@admin.register(models.oList)
class oListAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['word_count']
    filter_horizontal = ["obj"]
    
    def word_count(self,obj):
        return models.Word.objects.filter(olist=obj).count()
