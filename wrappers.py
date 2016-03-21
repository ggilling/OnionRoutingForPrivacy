class Wrappers:
      def queryWrap(query, pdsList, myKey, theirKey, gpg):
          ###### DO something different if they are queries to be checked? ######
          bundle = "<PDSList>"
          for aPDS in pdsList:
              bundle = bundle + "<PDS>" + str(aPDS) + "</PDS>"
          bundle = bundle + "</PDSList>"
          bundle = bundle + "<query>" + str(query) + "</query>"
          bundle = "<encrypted-block>" + str(gpg.encrypt(bundle, theirKey, sign = myKey)) + "</encrypted-block>"
          return bundle
              
##<encrypted-block>
          ##<PDSList>
          ##<PDS>PDS1</PDS>
          ##<PDS>PDS2</PDS>
          ##<PDS>PSN</PDS>
          ##</PDSList>
          ##<query>
          ## I'm a query!
          ##</query>
          ##</encrypted-block>
          pass
      def wrapGame(gameResult, myKey, theirKey, gpg):
          bundle = "<score>" + gameResult + "</score>"
          bundle = str(gpg.encrypt(bundle, theirKey, sign = myKey))
          bundle = "<encrypted-block>" + bundle + "</encrypted-block>"
          return bundle
          ## <encrypted-block>
          ## <score>gameResult!</score>
          ## </encrypted-block>

      def transmissionWrap(something):
          return "<transmission>" + something + "</transmission>"
