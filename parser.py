class Parser:
    def __init__(self):
        self.currentTag = ""
        self.transmission = {}
    def dexmlify(decryptedBlock):
# call this when a packet is received....
        p = xml.parsers.expat.ParserCreate()
        theParser = Parser()
        p.StartElementHandler = start_element
        p.EndElementHandler = end_element
        p.CharacterDataHandler = char_data
        p.Parse(decryptedBlock)
        return self.transmission

    def start_element(self, name, attrs):
        #    print 'Start element:', name, attrs
        self.currentTag = name
        print self.currentTag
        self.transmission[name] = ""

    def end_element(self, name):
        #    print 'End element:', name
        print "closed", self.currentTag
        self.currentTag = None
    def char_data(self, data):
    ##    print 'Character data:', repr(data)
    #    if currentTag == TRANSMISSION:
    #        pass
    #    elif currentTag == NEXT_HOP:
    ##self.next_hop = data
    #        print "Next Hop: ", data
    #    elif currentTag == ENCRYPTED_BLOCK:
    ## This is where the magic has to happen.
    #self.onion = decrypt(data)
    #        print "Encrypted Block: ", data
        self.transmission[self.currentTag].append(data)
        print self.currentTag, data
##### ##### ##### ##### ##### ##### ###### ##### #####
