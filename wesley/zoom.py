import django
import csv
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'wesley.settings')
django.setup()

from words.models import zoom

with open ('class.csv','r',encoding='utf-8-sig') as f:
    zoom.objects.all().delete()
    rd = csv.reader(f)
    for row in rd:
        c = row[0].replace('1.00E+','1E')
        try:
            tmp = zoom.objects.get_or_create(cLass=c,lInk=row[1],tEacher=row[2])
        except:
            print(row)
