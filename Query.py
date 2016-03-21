    # <transmission>
    # <source> an address </source>
    # <query>
    #       some stuff
    # </query>
    # <PDSList>
    #       <PDS> an address </PDS>
    #       <PDS> an address </PDS>
    #       <PDS> an address </PDS>
    # </PDSLIST>
    # </transmission>
TRANSMISSION = "transmission"
SOURCE = "source"
QUERY = "query"
PDSLIST = "PDSList"
PDS = "PDS"

class Query:
    def __init__(self, theQuery = "test", theSource = "localhost", theDestination, theIdentifier = "ID", thexmlified = None, theKey, theGPG):
        self.query = theQuery
        self.source = theSource
        self.key = theKey
        self.gpg = theGPG
        self.xmlified = thexmlified
        self.identifier = theIdentifier
        self.currentTag = ""
        self.pdsList = []
        self.destination = theDestination


### Get, set methods:
    def getDestination(self):
        return self.destination

    def getQuery(self):
        return self.query
    def setQuery(self, aQuery):
        self.query = aQuery

    def getSource(self):
        return self.source
    def setSource(self, aSource):
        self.source = aSource

    def getIdentifier(self):
        return self.identifier
    def setIdentifier(self, anIdentifier):
        self.identifier = anIdentifier

    def getPeers(self):
        return self.pdsList

    def dexmlify(self, source, sourceKey):
        ### this method decrypts and verifies the query and then parses the query into its destinations, query, source etc.
        p = xml.parsers.expat.ParserCreate()
        p.StartElementHandler = start_element
        p.EndElementHandler = end_element
        p.CharacterDataHandler = char_data

        p.Parse()


    # 3 handler functions

    # I'm going to need: a buffer of some sort?
    # think about this tonight.

    def start_element(name, attrs):
    #    print 'Start element:', name, attrs
        self.currentTag = name

    def end_element(name):
    #    print 'End element:', name
        self.currentTag = None
    def char_data(data):
    #    print 'Character data:', repr(data)
        if currentTag == TRANSMISSION:
            pass
        if currentTag == SOURCE:
            self.source = data
        elif currentTag == QUERY:
            self.query = data
        elif currentTag == PDS:
            ## This is where the magic has to happen.
            self.pdsList.append(data)

    def encrypt(self, destination, destKey):
        ### this method encrypts the query and returns an encrypted string.
        ### TODO: this is not quite right.
        encrypted = gpg.encrypt(self.query, destination, sign=self.key)
        return str(encrypted)

    def decrypt(self, source, sourceKey):
        ### this method decrypts the content of an xmlified encrypted block, and returns an unencrypted string.
        decrypted = gpg.decrypt(self.query, sign=sourceKey)
        if decryted.verified == True:
            return str(decrypted)
        else:
            return "ERROR - Signature not valid"



    def xmlify(self, destination, destKey, allDestinations):
        ## this method makes an xmlified, encrypted query to be sent to destination
                ### xmlifies the current message, building an onion as it goes.
        # open a file, write to it the xml-ified version of the query
        # structure:
        # <transmission>
        # <next-hop> a hop </next-hop>
        # <encrypted block>
        # (encrypted block contains one of these same blocks)
        # </encrypted block>
        # </transmission>

        # using xml.dom.minidom will autosanitize input!
        XMLQuery = Document()
        transmissionTag = XMLQuery.createElement(TRANSMISSION)
        XMLQuery.appendChild(transmissionTag)

        sourceTag = XMLQuery.createElement(SOURCE)
        transmissionTag.appendChild(sourceTag)
        sourceText = XMLQuery.createTextElement(self.source)
        next_hop.appendChild(sourceText)

        queryTag = XMLQuery.createElement(QUERY)
        transmissionTag.appendChild(queryTag)
        queryText = XMLQuery.createTextElement(self.query)
        queryTag.appendChild(queryText)

        PDSListTag = XMLQuery.createElement(PDSLIST)
        for aPDS in allDestinations:
            PDSTag = XMLQuery.createElement(PDS)
            PDSListTag.appendChild(PDSTag)
            PDSText = XMLQuery.createTextElement(aPDS)
            PDSTag.appendChild(PDSText)
        ## TODO: this little bit is maybe not quite right -- I don't know if this syntax is correct.
        ## TODO: this also needs to be encrypted!
        return XMLQuery.toxml()

