from django.contrib import admin
from . import models

admin.site.register(models.Word)
admin.site.register(models.Type)
admin.site.register(models.WordBook)
admin.site.register(models.sList)
admin.site.register(models.vList)
admin.site.register(models.oList)
