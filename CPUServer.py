from twisted.internet import ssl, reactor
from twisted.internet.protocol import ClientFactory, Protocol

PORT = 8000


class CPUClient(Protocol):
    def connectionMade(self):
        self.factory.CPU.connectedPDSList.append(self) ### TODO: think this through a little bit
        print "Connection to", self.transport.getPeer(), "established."
    def connectionLost(self, reason):
        self.factory.CPU.connectedPDSList.remove(self)
        print "Connection to", self.transport.getPeer(), "has been lost."

    def dataReceived(self, data):
        message = buildTransmission(self.factory, data)
        if message != None:
            ## TODO: fix this.
            self.factory.returnedMessages.append(message)
            self.factory.CPU.messageReceived(message)



    def send(data):
        self.transport.write(data)
        # self.transport.loseConnection(destination, self.port) ## TODO: Maybe??



class CPUClientFactory(Factory):
    protocol = CPUClient
    def __init__(self, aCPU):
        self.connectedPDSList = []
        self.currentTransmission = ""
        self.returnedMessages = []
        self.cpu = aCPU

    def sendToAll(data):
        ### TODO: this is not going to work.
        for aPDS in self.connectedPDSList:
            send(data, (aPDS, self.port))

if __name__ == '__main__':
    factory = CPUClientFactory()
    reactor.connectSSL('localhost', PORT, factory, ssl.ClientContextFactory())
#
    reactor.run()
