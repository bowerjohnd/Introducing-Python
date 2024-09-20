from twisted.internet import protocol, reactor

class Knock(protocol.Protocol) :
	print("start Knock class")
	def dataReceived(self, data) :
		print("start Knock.dataReceievd function")
		print('Client:', data)
		if data.startswith("Knock knock") :
			response = "Who's there?"
		else :
			response = data + " who?"
		print('Server:', response)
		self.transport.write(response)
		print("end Knock.dataReceived function")
	print("end Knock class")

class KnockFactory(protocol.Factory) :
	print("start KnockFactory class")
	def buildProtocol(self, addr) :
		print("start KnockFactory.buildProtocol function")
		return Knock()
		print("end KnockFactory.buildProtocol function")
	print("end KnockFactory class")

print("reactor.listen")
reactor.listenTCP(8000, KnockFactory())
print("reactor.run()")
reactor.run()

print("eof")