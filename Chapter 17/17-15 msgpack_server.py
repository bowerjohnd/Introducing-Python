import msgpackrpc

class Services(object) :
    def double(self, num) :
        return num * 2

server = msgpackrpc.Server(Services())
server.listen(msgpackrpc.Address("localhost", 6789))
server.start()