import django
import csv
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'wesley.settings')
django.setup()

from words.models import Word, Type

with open('word.csv','r', encoding='utf-8-sig') as f:
    rd = csv.reader(f)
    for row in rd:
        tmp = Word.objects.get_or_create(word_type = Type.objects.get(_type=row[0].capitalize()), word=row[1], mean = row[2])
