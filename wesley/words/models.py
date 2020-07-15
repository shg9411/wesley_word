from django.db import models
from django.urls import reverse

from django.conf import settings
import os

class Type(models.Model):
    _type = models.CharField(max_length = 20)
    
    def __str__(self):
        return self._type

def cp(instance,filename):
    fullname = os.path.join(settings.MEDIA_ROOT)+'{}/{}.jpg'.format(instance.word_type,instance.word).replace(' ','_')
    if os.path.exists(fullname):
        os.remove(fullname)
    return '{}/{}.jpg'.format(instance.word_type,instance.word)


class Word(models.Model):
    word_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    word = models.CharField(max_length = 20)
    image = models.ImageField(blank=True, upload_to=cp)
    mean = models.CharField(max_length = 20, blank = True)
    class Meta:
        ordering = ['word',]
        constraints = [
            models.UniqueConstraint(fields = ['word_type','word'],name='unq')
        ]

    def __str__(self):
        return '{},{},{}'.format(self.word,self.mean,self.word_type)

    def get_absolute_url(self):
        return reverse('word-detail',kwargs={'pk':self.pk})

class sList(models.Model):
    theme = models.CharField(max_length = 20)
    subject = models.ManyToManyField(Word)
    
    def __str__(self):
        return self.theme

class vList(models.Model):
    theme = models.CharField(max_length = 20)
    verb = models.ManyToManyField(Word)

    def __str__(self):
        return self.theme


class oList(models.Model):
    theme = models.CharField(max_length = 20)
    obj = models.ManyToManyField(Word)

    def __str__(self):
        return self.theme

class WordBook(models.Model):
    teacher = models.CharField(max_length = 20)
    _class = models.CharField(max_length = 20)
    title = models.CharField(max_length = 20)
    subjects = models.ForeignKey(sList,null=True,blank = True, on_delete=models.CASCADE)
    verbs = models.ForeignKey(vList,null=True,blank = True, on_delete=models.CASCADE)
    objs = models.ForeignKey(oList,null=True,blank = True, on_delete=models.CASCADE)
    description = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return "{} {} {}".format(self.teacher,self._class,self.title)
