import zerorpc

class RPC() :
    def double(self, num) :
        return 2 * num

server = zerorpc.Server(RPC())
server.bind("tcp://localhost:4242")
server.run()