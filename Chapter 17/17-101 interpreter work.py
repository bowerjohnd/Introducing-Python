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
