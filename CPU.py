END_TAG = "</transmission>"

class CPU:
    def __init__(self, theQuery = None, theCloud, theKeys, theKey, theGPG, theClient, theID):
        self.query = theQuery
        self.cloud = theCloud
        self.keys = theKeys
        self.gpg = theGPG
        self.myKey = theKey
        self.client = theClient
        self.id = theID
        self.message = None
        self.transmissions = {}

    def newQuery(theQuery = "test", theSource = "localhost", theIdentifier = "ID", thexmlified = None, theKey, theGPG):
        self.query = Query(theQuery, theSource, theIdentifier, myKey, gpg)

    def sendQuery(self, theQuery, thePDSs = self.cloud):
        for aServer in thePDSs:
            ###TODO: this is not currently how this will work
            theQuery.xmlify(aServer, aServer.getKey(), self.key(), thePDSs)
            self.client.send(aServer, theQuery)

    def messageReceived(self, theMessage, theSource):
        ### if this is in fact a response to our query, let's return it.
        self.message = theMessage.decrypt(theSource)
        return self.message

    def buildTransmission(self, data, source):
        if self.transmissions[source] != None:
            self.transmissions[source].append(data)
        else:
            self.transmissions[source] = data
        if END_TAG in transmissions[source]:
            transmissionKind = getKind(transmissions[source])
            if transmissionKind == "message":
                messageReceived(transmissions[source], source)
            elif transmissionKind == "coordinator-setter":
                self.coordinator = source
            else:
                ### TODO: make an error type, handler that will deal w/ this.
                pass
