class Coordinator:
    def __init__(self, aPDS, aCloud, aQuery):
        self.PDS = aPDS
        self.cloud = aCloud
        self.query = aQuery
        self.queries = []

    def receiveQuery(self, aPDS, query):
        self.queries[aPDS] = query
        if len(self.queries()) > aPDS.getTolerance()):
            return sameQueries()

    def sameQueries(self):
        sameHosts = [self.PDS]
        for aQuery in self.queries:
            if self.query.decrypted() == aQuery.decrypted():
                sameHosts.append(aQuery.getsource())
        return sameHosts

    def sendToAll(self):
        for aPDS in self.cloud:
            self.PDS.sendTo(aPDS, sameQueries())
 

    
