#    def buildTransmission(self, data):
        #todo here: make sure to use get, set methods instead of directly addressing variable
#        if startTag in line and currentTransmission != "":
            # this line starts a new transmission, but we already have one going on
#            print "Error: received new transmission before old one finished."
#        else:
#            entity.currentTransmission = entity.currentTransmission + line
#            if endTag in line and entity.currentTransmission == "":
                #This line ends a transmission, but no data has actually been received yet
#                print "Error: received End of Transmission before data."
#            elif endTag in line:
                # TODO: decrypt transmission
                # additionally, get rid of currentTransmission
#                result = decrypt(transmission)
#                entity.currentTransmission = ""
#                return result
#        return None

#    def sendQuery(self, query):
#        wrappedQuery = wrapQuery(query)
#        for aPDS in self.factory.connectedPDSList:
#            self.transport.write(query, #aPDS
#                                 )
#            self.transport.LoseConnection()
