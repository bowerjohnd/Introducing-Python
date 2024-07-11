import time

now = time.time()
print(now)
print(time.ctime(now))

print("")

fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
print(t)
print(time.strftime(fmt, t))

print("")

from datetime import date

some_day = date(2019, 7, 4)
print(some_day.strftime(fmt))

print("")

from datetime import time

some_time = time(10, 35)
print(some_time.strftime(fmt))

print("")

import time

fmt = "%Y-%m-%d"
#print(time.strptime("2019 01 29", fmt))
print(time.strptime("2019-01-29", fmt))

fmt = "%Y %m %d"
print(time.strptime("2019 01 29", fmt))
#print(time.strptime("2019 13 29", fmt))

print("")

import locale
from datetime import date

halloween = date(2019, 10, 31)

for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is',] :
	locale.setlocale(locale.LC_TIME, lang_country)
	print(halloween.strftime('%A, %B %d'))

names = locale.locale_alias.keys()
good_names = [name for name in names if \
len(name) == 5 and name[2] == '_']

print(good_names)
print(len(good_names))

de = [name for name in good_names if name.startswith('de')]
print(de)

