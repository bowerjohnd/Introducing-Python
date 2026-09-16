# This script is mean to be run line-by-line in the python interpreter

import socket

# Internet Services - DNS
print()
print(socket.gethostbyname('www.crappytaxidermy.com'))
print(socket.gethostbyname_ex('www.crappytaxidermy.com'))
print()
print(socket.getaddrinfo('www.crappytaxidermy.com', 80))
print(socket.getaddrinfo('www.crappytaxidermy.com', 80, socket.AF_INET, socket.SOCK_STREAM))
print()
print(socket.getservbyname('http'))
print(socket.getservbyport(80))

# Data Serialization - Serialize with pickle

import pickle
import datetime

now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)

print('-----------')
print(now1)
print(now2)
print('-----------')

#import pickle

class Tiny() :
    def __str__(self) :
        return 'tiny'

obj1 = Tiny()
print(obj1)
print(str(obj1))
print('')

pickled = pickle.dumps(obj1)
print(pickled)
print('')

obj2 = pickle.loads(pickled)
print(obj2)
print(str(obj2))