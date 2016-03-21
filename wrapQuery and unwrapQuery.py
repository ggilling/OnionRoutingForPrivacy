def wrapQuery(query, myKey, theirKey, gpg):
    wrappedQuery = str(gpg.encrypt(query, theirKey, sign = myKey))
    return wrappedQuery

def unwrapQuery(query, myKey, theirKey, gpg):
    decrypted = gpg.decrypt(query, myKey, sign=theirKey)
    if gpg.decrypt(query, myKey, sign=theirKey):
        return decrypted
    else:
        return "Error: Unverified Signature."


