import csv
import pandas as pd
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "management.settings")
import django
django.setup()

from lecture.models import Lecture


CSV_PATH = 'static/file/udacity.csv'


with open(CSV_PATH, 'r', newline='') as csvfile:
	data_reader = csv.DictReader(csvfile)
	s = pd.DataFrame(data_reader)

ss = []
for i in range(len(s)):
	st = (s['title'][i], s['content'][i], s['category'][i], s['level'][i], s['period'][i], s['student'][i], s['skill_covered'][i], s['pre_ready'][i])
	ss.append(st)
for i in range(len(s)):
	Lecture.objects.create(class_name=ss[i][0], content=ss[i][1], level=ss[i][3], period=ss[i][4], student=ss[i][5], subject=ss[i][6], pre_ready=ss[i][7])
