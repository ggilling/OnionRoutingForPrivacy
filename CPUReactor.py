### This file contains the reactor Loop, into which stuff will be plugged.
### Hopefully.

def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

10001 10002 10003

to grab data from servers on ports 10001, 10002, and 10003.

Of course, there need to be servers listening on those ports
for that to work.
"""

    parser = optparse.OptionParser(usage)

    _, addresses = parser.parse_args()

    if not addresses:
        print parser.format_help()
        parser.exit()

    def parse_address(addr):
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)

        if not port.isdigit():
            parser.error('Ports must be integers.')

        return host, int(port)

    return map(parse_address, addresses)


class CPUProtocol(Protocol):

    response = ''

    def dataReceived(self, data):
        self.response += data

    def connectionLost(self, reason):
        self.responseReceived(self.response)

    def responseReceived(self, response):
        self.factory.response_finished(response,)


class CPUClientFactory(ClientFactory):

    protocol = CPUProtocol

    def __init__(self, deferred):
        self.deferred = deferred

    def response_finished(self, response):
        if self.deferred is not None:
            ### If the response is finished, then set the current deferred to be nothing - we don't need to add a callback
            d, self.deferred = self.deferred, None
            d.callback(response)

    def clientConnectionFailed(self, connector, reason):
        if self.deferred is not None:
            d, self.deferred = self.deferred, None
            d.errback(reason)


def get_responses(host, port, query):
    """
    Download a poem from the given host and port. This function
    returns a Deferred which will be fired with the complete text of
    the poem or a Failure if the poem could not be downloaded.
    """
    d = defer.Deferred()
    from twisted.internet import reactor
    factory = CPUClientFactory(d)
    reactor.connectTCP(host, port, factory)
    
#    reactor.connectTCP(host, port, factory)
    return d


def cpu_main():
    addresses = parse_args()

    from twisted.internet import reactor

    responses = []
    errors = []

    def got_response(response):
        responses.append(decrypt(response)) #TODO.

    def response_failed(err):
        print >>sys.stderr, 'Failed in getting response from server:', err
        errors.append(err)

    def responses_done(_):
        ## The logic here might not work out - do we really want all of the servers to respond that they know nothing?
        if len(responses) + len(errors) == len(addresses):
            reactor.stop()

    for address in addresses:
        host, port = address
        d = get_responses(host, port, query)
        d.addCallbacks(got_response, response_failed)
        d.addBoth(responses_done)

    reactor.run()

    for response in responses:
        print response


if __name__ == '__main__':
    cpu_main()
