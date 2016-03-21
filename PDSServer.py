### TODO for tomorrow: Make a query-handler object - right now the server is only assuming that it's handling one query at a time - really it could be handling many. Make sure that there's a query identifier number, and that these are not necessarily sequential, but perhaps depends upon a few things.
### TODO: make decryption function wrapper
### TODO: make sure that your deonionifying function works.
### TODO: make the client work.
### TODO: deal with TODO's.
### TODO: handle keyrings/identities


from twisted.internet import ssl, reactor
from twisted.internet.protocol import Factory, Protocol

PORT = 8000

class PDSServer(Protocol):

    def connectionMade(self):
        source = self.transport.getPeer()
        ## This is wrong.
        theQuery = Query(theSource = source)

    def dataReceived(self, data):
        ### build a transmission out of the data we just got - make sure to associate it with the server with whom we are making a connection.
        source = self.transport.getPeer()
        self.factory.currentTransmission.buildTransmission(data, source)

#        """When data is received, build a transmission object out of it."""
#        thePackage = self.buildTransmission(self, data)
#        thePackage = dexmlify(thePackage)
#        if isNewQuery(thePackage):
#            self.newQueryHandler(thePackage)
            ## TODO: add a callbacklater call here that sees if the query has been verified by all the participating data sources until all PDS's have said that they've gotten it. Count this number until COMFORT has been met.

#        if isOnion(thePackage):
#            self.deOnion(thePackage)

        def connectionLost(self):
            self.factory.connectionsList.remove(self)


class PDSServerFactory(Factory):
    def __init__(self, aPDS):
#    def __init__(address, name, keyRing):
#        self.address = address
#        self.name = name
#        self.keyRing = keyRing
#        self.peers = []
        ### TODO: extract all the peers from the keyring?? self.peers = keyRing
        self.currentTransmission = ""
        self.receivedTransmission = {}
#        self.connectionsList = []


        self.PDS = aPDS

    def buildTransmission(self, data, source):
        aPDS.buildTransmission(data, source)
        

    def dexmlify(decryptedBlock):
        # call this when a packet is received....
        p = xml.parsers.expat.ParserCreate()
        p.StartElementHandler = start_element
        p.EndElementHandler = end_element
        p.CharacterDataHandler = char_data

        p.Parse()


    # 3 handler functions
    # start_element deals with the kind of tag that is just <tag>
    # end_element deals with the kind of tag that is </tag>
    # char_data deals with text elements.

    # I'm going to need: a buffer of some sort?
    # think about this tonight.

     def start_element(name, attrs):
    #    print 'Start element:', name, attrs
        self.currentTag = name

     def end_element(name):
    #    print 'End element:', name
        self.currentTag = None
     def char_data(data):
         ### Adds the data to the current transmission...
    #    print 'Character data:', repr(data)
         if self.receivedTransmission[self.currentTag] != None:
             self.receivedTransmission[self.currentTag].append(data)
         else:
             self.receivedTransmission[self.currentTag] = data

    def isGameResults(aPackage):
        return "score" in aPackage.keys()
    def gameHandler(aPackage):
        ### self.pds.tallyResults(aPackage["source"], aPackage["score"]
        pass

    def isNewQuery(aPackage):
        return "query" in aPackage.keys()

    def newQueryHandler(aPackage):
        for aPDS in aPackage["PDS"]:
            signedEncrypted = signAndEncrypt(aPackage["query"], aPDS)
            connectToandSend(aPDS, signedEncrypted)
    def signAndEncrypt(query, recipient):
        ### TODO: This needs to be distinctively XML'd probably

        pass

    def connectToandSend(recipient, query):
        ### TODO: Send query to the recipient - you'll probably need to have an associated factory, and an associated client. :\
        # connectSSL(recipient, port, otherargs)
        # self.write(query)

        pass
    def isOldQuery(aPackage):
        ### there's an encrypted block in here, but no next-hop argument
        return "encrypted-block" in aPackage.keys() and not "next-hop" in aPackage.keys()
    def oldQueryHandler(aPackage):
        # TODO: implement this in actual fact; don't just fake it as I've done here
        # theirQuery = decrypt(aPackage["query"])
        # if theirQuery == self.query:
        #      otherRecipients += 1
        
    def isOnion(aPackage):
        return "next-hop" in aPackage.keys()
        
    def deOnion(aPackage):
        ### TODO: make sure that the logic here makes sense. I'm not sure it does.

        signedEncrypted = signAndEncrypt(aPackage["encrypted-block"])
        connectToandSend(aPackage["next-hop"], signedEncrypted)
        

    def buildTransmission(self, data):
        #todo here: make sure to use get, set methods instead of directly addressing variable
        if startTag in line and entity.currentTransmission != "":
            # this line starts a new transmission, but we already have one going on
            print "Error: received new transmission before old one finished."
        else:
            entity.currentTransmission = entity.currentTransmission + line
            if endTag in line and entity.currentTransmission == "":
                #This line ends a transmission, but no data has actually been received yet
                print "Error: received End of Transmission before data."
            elif endTag in line:
                # TODO: decrypt transmission
                # additionally, get rid of currentTransmission
                result = decrypt(transmission)
                entity.currentTransmission = ""
                return result

if __name__ == '__main__':
    factory = Factory()
    factory.protocol = Echo
    reactor.listenSSL(PORT, factory,
                      ssl.DefaultOpenSSLContextFactory(
            'keys/server.key', 'keys/server.crt'))
    reactor.run()
