# book wants you to start this on a Mac..

import os
#print(os.uname())
#print(os.getloadavg())
print(os.cpu_count())

print("")

# os.system('date -u')

# pip install psutil for the next instruction

import psutil
print(psutil.cpu_times(True))

print(psutil.cpu_percent(True))
print(psutil.cpu_percent(percpu=True))

# pip install invoke for the next instruction

# see tasks.py