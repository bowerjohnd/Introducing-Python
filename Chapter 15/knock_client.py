# errors occur in KnockClient connectionMade function, after knock_server returns Knock()
#	- builtins.TypeError: Data must be in bytes

from twisted.internet import reactor, protocol

class KnockClient(protocol.Protocol) :
	print("start client KnockClient class")
	def connectionMade(self) :
		print("start client KnockClient.connectionMade function")
		self.transport.write("Knock knock")
		print("end client KnockClient.connectionMade function")

	def dataReceived(self, data) :
		print("start client KnockClient.dataReceived function")
		if data.startswith("Who's there?") :
			print("data does start with Who's there?")
			response = "Disappearing client"
			self.transport.write(response)
		else :
			print("data does not start with Who's there?")
			self.transport.loseConnection()
			reactor.stop()
		print("end client KnockClient.dataReceieved function")
	print("end client KnockClient class")

class KnockFactory(protocol.ClientFactory) :
	print("start client KnockFactory class")
	protocol = KnockClient
	print("end client KnockFactory class")

def main() :
	print("start client main")
	f = KnockFactory()
	reactor.connectTCP("localhost", 8000, f)
	reactor.run()
	print("end client main")

if __name__ == '__main__' :
	main()