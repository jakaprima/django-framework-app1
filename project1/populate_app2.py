#buat populate pake library faker
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')

import django
django.setup()

## fake pop script
import random
from app2.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ['search', 'social', 'marketplace', 'news', 'games']

def add_topic():
	t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t

def populate(N=5):
	for entry in range(N):
		#get topic dari entry
		top = add_topic()
		#buat fake data untuk entry
		fake_url = fakegen.url()
		fake_date = fakegen.date()
		fake_name = fakegen.company()

		#create webpage entry baru
		webpg = Webpage.objects.get_or_create(topic=top, url= fake_url, name=fake_name)[0]

		#buat fake access recored dari webpage
		acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0] # webpg karena foreign key

if __name__ == '__main__':
	print('populasi script')
	populate(20)
	print('populate selesai')
