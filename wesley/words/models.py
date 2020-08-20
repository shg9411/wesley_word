from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.cache import cache
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

    @property
    def type(self):
        return self.word_type._type

    def __str__(self):
        return '{},{},{}'.format(self.word,self.mean,self.word_type)

    def get_absolute_url(self):
        return reverse('word-detail',kwargs={'pk':self.pk})

    def save(self, *args, **kwargs):
        print("del",cache.delete('words'))
        super().save(*args,**kwargs)

class sList(models.Model):
    subject = models.ManyToManyField(Word)

class vList(models.Model):
    verb = models.ManyToManyField(Word)

class oList(models.Model):
    obj = models.ManyToManyField(Word)

class WordBook(models.Model):
    teacher = models.CharField(max_length = 20)
    _class = models.CharField(max_length = 20)
    title = models.CharField(max_length = 20)
    subjects = models.ForeignKey(sList,null=True,blank = True, on_delete=models.CASCADE)
    verbs = models.ForeignKey(vList,null=True,blank = True, on_delete=models.CASCADE)
    objs = models.ForeignKey(oList,null=True,blank = True, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.teacher,self._class,self.title)


class zoom(models.Model):
    cLass = models.CharField(max_length = 10)
    tEacher = models.CharField(max_length = 50)
    lInk = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.cLass
