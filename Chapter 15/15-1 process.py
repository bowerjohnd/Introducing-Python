# most of this doesn't work for me in windows command prompt, most likely need linux terminal

import os

print(os.getpid())
print(os.getcwd())
#print(os.getuid())
#print(os.getgid())

import subprocess

ret = subprocess.getoutput('date')
print(ret)

ret = subprocess.getoutput('date -u')
print(ret)

#ret = subprocess.getoutput('date -u | wc')
print(ret)

#ret = subprocess.check_output(['date', '-u'])
print(ret)

ret = subprocess.getstatusoutput('date')
print(ret)

#ret = subprocess.call('date')
print(ret)

ret = subprocess.call('date -u', shell=True)
print(ret)

#ret = subprocess.call(['date', '-u'])
print(ret)

