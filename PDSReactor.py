import optparse, os

from twisted.internet.protocol import ServerFactory, Protocol

## TODO: change usage-string.
def parse_args():
    usage = """usage: %prog [options] database-file
python [port] database-file
"""
#This is the Fast Poetry Server, Twisted edition.
#Run it like this:

#  python fastpoetry.py <path-to-poetry-file>

#If you are in the base directory of the twisted-intro package,
#you could run it like this:

#  python twisted-server-1/fastpoetry.py poetry/ecstasy.txt

#to serve up John Donne's Ecstasy, which I know you want to do.


    parser = optparse.OptionParser(usage)

    help = "The port to listen on. Default to a random available port."
    parser.add_option('--port', type='int', help=help)

    help = "The interface to listen on. Default is localhost."
    parser.add_option('--iface', help=help, default='localhost')

    options, args = parser.parse_args()

    if len(args) != 1:
        parser.error('Provide exactly one poetry file.')

    poetry_file = args[0]

    if not os.path.exists(args[0]):
        parser.error('No such file: %s' % poetry_file)

    return options, poetry_file

################### CHANGE THE ABOVE!!!!! #############################

class PDSProtocol(Protocol):

    def connectionMade(self):
        ### This is not quite right.
        if self.transport.getPeer() in knownPDSs:
            self.factory.connectedPDSs.append(self)
        else:
            self.factory.connectedCPUs.append(self)
        
        #self.transport.write(self.factory.poem)
        #self.transport.loseConnection()

    def dataReceived(self, data):
        if self.transport.getPeer() in self.factory.connectedCPUs:
            query = data
            handleQuery(query, self.transport.getPeer())
        if self.transport.getPeer() in self.factory.connectedPDSs:
            message = data
            handleMessage(message, self.transport.getPeer())

    def connectionLost(self):
        myAddress = self.transport.getPeer()
        if myAddress in self.factory.connectedCPUs:
            self.factory.connectedCPUs.remove(myAddress)
        elif myAddress in self.factory.connectedPDSs:
            self.factory.connectedPDSs.remove(myAddress)
    def handleQuery(self, query, host):
        ### PASTE QUERY HANDLER CODE HERE ###
        decrypt(query, host) # add keys?

    def handleMessage(self, host):
        ### PASTE MESSAGE HANDLER CODE HERE ###

class PDSFactory(ServerFactory):

    protocol = PDSProtocol

    def __init__(self, database):
        self.database = database
    ### PASTE IN KEY STUFF, GPG STUFF HERE ###

def main():
    options, poetry_file = parse_args()

    poem = open(poetry_file).read()

    factory = PoetryFactory(poem)

    from twisted.internet import reactor


    port = reactor.listenTCP(options.port or 0, factory,
                             interface=options.iface)



#    print 'Serving %s on %s.' % (poetry_file, port.getHost())

    reactor.run()

def get_same_queries(host, port, query):
    """
    Send a query to a host on a port to see if they got the same query.
    """
    d = defer.Deferred()
#    from twisted.internet import reactor
    factory = PDSServerFactory(d)
    reactor.connectTCP(host, port, factory) ## TODO: this is going to raise an error right now
    #### PASTE query-wrapping code here ####
#    reactor.connectTCP(host, port, factory)
    return d

def send(message, server):
    ### encrypt this business, slap a transmission tag on it, let it go. ###
    ## PASTE SENDY-CODE IN HERE ###


if __name__ == '__main__':
    main()
