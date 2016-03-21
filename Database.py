aList = range(0, 100)
dictionary = {}
for item in aList:
    dictionary[item] = item



class Database:
      def __init__(self, aDictionary=dictionary):
          self.database = aDictionary

      def query(self, query, aDictionary):
          ### TODO: Hmmm. I'm not really sure how this is going to work. SQL? For now, just return the database.
          return self.database
