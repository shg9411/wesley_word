from django.contrib import admin
from . import models



@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display=['word','mean']
    list_filter = ('word_type',)
    search_fields = ['word']
    ordering = ('word',)

@admin.register(models.WordBook)
class WordBookAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['title','description']
    search_fields = ['title']
    ordering = ('title',)

    fieldsets = [
        ('Title', {'fields':['title']}),
        ('List',{'fields':['subjects','verbs','objs']}),
        ('Description',{'fields':['description']}),
    ]

@admin.register(models.sList)
class sListAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['theme','word_count']
    filter_horizontal = ["subject"]
    def word_count(self,obj):
        return models.Word.objects.filter(slist=obj).count()

@admin.register(models.vList)
class vListAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['theme','word_count']
    filter_horizontal = ["verb"]

    def word_count(self,obj):
        return models.Word.objects.filter(vlist=obj).count()

@admin.register(models.oList)
class oListAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['theme','word_count']
    filter_horizontal = ["obj"]
    def word_count(self,obj):
        return models.Word.objects.filter(olist=obj).count()
