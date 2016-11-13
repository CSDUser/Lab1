import re
import requests

mas1 = set()
mas2 = set()
mas2_Old = set()
url1 = 'http://www.mosigra.ru/'
max = 0

def func(url):
	r = requests.get(url)
	with open('test.html', 'w') as output_file:
		output_file.write(r.text.encode('cp1251'))			
	f1 = open("test.html",'r')	
	for line in f1.readlines():	
		a = re.search(r'(?<=\b)\w([\w\.\-_0-9])*(@| at )[\w0-9][\w\-_0-9]*((\.| DOT )[\w\-_0-9]+)+(?=\b)', line)  #mail
		b = re.search(r'http://www.mosigra.ru/+[a-zA-Z/]+(?::\d)?', line)  #url
		if a:
			mas1.add(a.group(0)) #constantly adds new different emails
		if b:
			mas2.add(b.group(0)) 	
	global max
	max = max+1		
	if max == 200: #limiter
		return
		
	i = 0
	for line in mas2:	
		a = line		
		if a in mas2_Old:
			h = 0
		else:
			mas2_Old.add(a)
			func(a)

	
	

func(url1)

			
print('Mails:')	
print(mas1)		
print('URLs:')	
print(mas2)	
print('All_URLs:')	
print(mas2_Old)	
	
		