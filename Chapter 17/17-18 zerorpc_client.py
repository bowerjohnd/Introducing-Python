import zerorpc

client = zerorpc.Client()
client.connect("tcp://localhost:4242")

num = 7

result = client.double(num)
print("Double", num, "is", result)