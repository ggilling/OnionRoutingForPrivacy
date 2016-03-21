import gnupg
from xml.dom.minidom import Document
import xml.parsers.expat

TRANSMISSION = "transmission"
NEXT_HOP = "next-hop"
MESSAGE = "message"
ENCRYPTED_BLOCK = "encrypted-block"

homeDirectory = "/keys"
gpg = gnupg.GPG(gnupghome = homeDirectory)
currentTransmissionDeTagged = {"next-hop":None, "encrypted-block":None, transmission}

class Message:
    def __init__(self, theRow = None, theRoute = None, theNextHop = None, theOnion = None, theKeys, theGPG):
        self.row = theRow
        self.route = theRoute
        self.keys = theKeys
        self.xmlified = theXMLified
        self.nexthop = theNextHop
        self.gpg = theGPG
        self.message = self.row
        self.onion = theOnion

    def onionify(self):
        for aHost in reversed(route):
            ### We want the original CPU's address at the heart of the onion.
            encryptedMessage = encrypt(self.message)
            self.message = xmlify(aHost, encryptedMessage)
        self.onion = message
        return self.onion

    def deonionify(self, theKey):
        ### this decrypts an onion, sets nextHop, returns the new, signed onion.
        dexmlified = dexmlify(self.onion)
        theOnion = 
        pass

    def xmlify(self, aHost, encryptedMessage):
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
        PDSMessage = Document()
        transmission = doc.createElement(TRANSMISSION)
        PDSMessage.appendChild(transmission)

        next_hop = doc.createElement(NEXT_HOP)
        transmission.appendChild(next_hop)
        nextHopText = doc.createTextElement(aHost)
        next_hop.appendChild(nextHopText)

        encrypted_block = doc.createElement(ENCRYPTED_BLOCK)
        transmission.appendChild(encrypted_block)
        encryptedText = doc.createTextElement(encryptedMessage)
        encrypted_block.appendChild(encryptedText)
        ## TODO: this little bit is maybe not quite right -- I don't know if this syntax is correct.
        return PDSMessage.toxml()


    def dexmlify(decryptedBlock):
        # call this when a packet is received....
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
        currentTag = name

    def end_element(name):
    #    print 'End element:', name
        currentTag = None
    def char_data(data):
    #    print 'Character data:', repr(data)
        if currentTag == TRANSMISSION:
            pass
        elif currentTag == NEXT_HOP:
            self.next_hop = data
        elif currentTag == ENCRYPTED_BLOCK:
            ## This is where the magic has to happen.
            self.onion = decrypt(data)

    def decrypt(self, data):
        ## TODO: make sure this works.
        decrypted = self.gpg.decrypt(data, self.key) # TODO: some of these variables don't actually exist.
        if decrypted.verified:
            return str(decrypted)
        else:

            ## TODO: make this throw an error.
            return "ERROR - INVALID SIGNATURE"

    def encrypt(self, data):
        encrypted = self.gpg.encrypt(data, self.nextHop, sign=self.key)
        return encrypted


def onionize(destCPU, randomRoute, message):
    layers = [destCPU] + reversed(randomRoute)
    # we want to make sure that the destination CPU's address is at the center of the onion, along with the encrypted message. 
    onion = message
    for layer in layers:
        onion = xmlify(layer["address"], gpg.encrypt(onion, layer["key"]))
    return onion

def peel(encryptedMessage, myKeySignature, theirKeySignature):
    decryptedMessage = gpg.decrypt(encryptedMessage, keySignature)
    verified = decryptedMessage.valid
    return str(decryptedMessage)
    


