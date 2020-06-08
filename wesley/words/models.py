from django.db import models


class Type(models.Model):
    Type = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.Type



class Word(models.Model):
    word_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    word = models.CharField(max_length = 20)
    image = models.ImageField(blank=True)
    mean = models.CharField(max_length = 20, blank = True)
    
    class Meta:
        ordering = ['word',]

    def __str__(self):
        if self.mean:
            return '/media/{}.jpg,{}'.format(self.word,self.mean)
        return '/media/{}.jpg'.format(self.word)


class sList(models.Model):
    subject = models.ManyToManyField(Word)

class vList(models.Model):
    verb = models.ManyToManyField(Word)

class oList(models.Model):
    obj = models.ManyToManyField(Word)

class WordBook(models.Model):
    title = models.CharField(max_length = 20)
    subjects = models.ForeignKey(sList,null=True,blank = True, on_delete=models.CASCADE)
    verbs = models.ForeignKey(vList,null=True,blank = True, on_delete=models.CASCADE)
    objs = models.ForeignKey(oList,null=True,blank = True, on_delete=models.CASCADE)
    description = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.title