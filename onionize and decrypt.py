## take a random route....

def layerEncryption(route, row, keyDictionary, aGPG):
    onion = row
    for aHop in reversed(route):
        onion = str(aGPG.encrypt(onion, keyDictionary[aHop]))
    	onion = "<next-hop>" + str(aHop) + "</next-hop>" + "<encrypted-block>" + onion + "</encrypted-block>"
#    onion = "<transmission>" + onion + "</transmission>"
    return onion

def decrypt(block, key, gpg):
    decrypted = gpg.decrypt(block)
    if decrypted.verified == True:
        return str(decrypted)
    else:
        return "Error verifying encrypted string."
