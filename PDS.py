END_TAG = "</transmission>"
import Random

class PDS:
   def __init__(self, thePort = 8000, theIdentifier = "Charlie", theKeys, theGPG, theDatabase = Database(), theServer, theCloud, theTolerance = 4):
       self.port = thePort
       self.identifier = theIdentifier
       self.database = theDatabase
       self.server = theServer
       self.keys = theKeys
       self.gpg = theGPG
       self.responses = []
       self.cloud = theCloud
       self.myKey = None ## TODO: link entities with their keys
       self.tolerance = theTolerance
       self.knownPeers = 0
       self.transmissions = {}
       self.game = []

   def getGPG(self):
      return self.gpg
   def setGPG(self, aGPG):
      self.gpg = aGPG
   
   def queryDatabase(self, query):
       self.responses = database.query(query)

   def playgame(self):
      winners = None
      while len(winners) != 0:
         myScore = sum([Random.random() for x in range(0, 10)])
         myScore = "<transmission><source>" + self.identifier + "</source><score>" + myScore + "</score></transmission>"
         for aPDS in self.cloud:
## TODO: make sure that you add a callback for this - everyone needs to have responded before the winner can be assigned.
            ## TODO: sendTo(aPDS(myScore))
            ## TODO: tallyResults(score, aPDS)
            ## TODO: self.coordinator = assignWinner(game)
            pass
         return winners[0]

   def tallyResults(aPDS, aResult):
      self.game[aPDS] = aResult

   def assignWinner(game):
      maxScore = None
      winners = []
      for aPDS in game.keys():
         if game[aPDS] > maxScore:
            winners = [aPDS]
         elif game[aPDS] == maxScore:
            winners.append(aPDS)
      return winners
         

   def makeAndSendMessage(self):

      ### TODO: THIS IS PROBABLY SLOPPY - returns true if there was a success, false otherwise.
      if knownPeers >= theTolerance:
          for aRow in self.responses:
              theRoute = Crypto.Random.random.sample(theCloud)
              if self.Coordinator != None:
                  theRoute.append(self.Coordinator)
### TODO: make this next bit into a send function, because in all likelihood it gets repeated below...

              theMessage = Message(aRow, theRoute, theKeys, gpg) ## TODO: does this make sense?
              theMessage.onionify()
              self.server.connect(self.Port, theRoute[0], factory argument) ### TODO: fix this call
              self.server.send(theMessage)
              self.server.loseConnection()
          return True
      else:
         return False

   def buildTransmission(self, data, source):
      if self.transmissions[source] != None:
         self.transmissions[source].append(data)
      else:
         self.transmissions[source] = data
      if END_TAG in data:
         transmissionKind = getKind(transmissions[source])
         if transmissionKind == "query":
            ## TODO: do some Query-type stuff
            handleQuery(transmission[source], source)

         elif transmissionKind == "onion":
            ## TODO: do some deonionification
            handleOnion(transmission[source], source)

         elif transmissionKind == "checkQuery":
            ## TODO: make sure that we've asked about this query/received it.... wait for one I guess if it hasn't gotten here yet.
            handleCheckedQuery(transmission[source], source)
         elif transmissionKind == "gameResults":
            handleGameResults(transmission[source], source)
         else:
            ## TODO: raise some kind of error here.
            pass

   def checkNumberOfRecipients(self, query, aCloud):
       total = 0
       for aServer in aCloud:
           ### TODO: make a deferred/call-back here
           query.signandEncrypt(self.myKey, aServer, gpg)
           self.server.connect(self.Port, aServer, factory argument) ### TODO: fix this call
           self.server.send(theMessage)
           self.server.loseConnection()
           ## TODO: if the server responds that they got the same query, then add this to the total
           ## add callback to sameQuery.... add up all the total += int(sameQuery(q1, q2))'s
           ## knownPeers.append(source of incoming same query)
       return total

   def receivePeersFromCoordinator(self, peers):
      knownPeers = peers
           
   def sameQuery(self, myQuery, theirQuery):
      return myQuery.decrypted() == theirQuery.decrypted()

   def handleOnion(self, onion, source):
      ### Ooo, a message! Deonionify it, send it to the next place.
      onion.deonionify(source)
      self.server.connect(self.Port, message.getNextHop(), factory argument) ### TODO: fix this call
      self.server.send(theMessage)
      self.server.loseConnection()

   def handleQuery(self, query, source):
      query.dexmlify()
      cloud = query.getPeers() ## note: self.cloud may already exist and so maybe you need to do something else here.
      if len(cloud) > LARGE_NUMBER_OF_PEERS:
         winner = playGame()
         self.coordinator = winner
         checkNumberOfRecipients(query, [self.coordinator])
         ## receivePeersFromCoordinator(peers)
      else:
         checkNumberOfRecipients(query, cloud)
      
      
      ## TODO:
      ## Pseudo-code here because I am fried:
      ## ok so:
      ## If there is a coodrinator, encrypt and send the query to the coordinator, and wait for response.
      ## othewrise: send query to everyone, wait for queries to pour in.
      ## if query is had by enough PDS's, then proceed to decrypt the query, see if we have something to respond to it.
      ## blergh.
