import gnupg
gpgHome = "/usr/local/bin/gpg"
theGpg = gnupg.GPG(gpgHome)
servers = ["10001", "10002", "10003", "10004", "10005", "10006"]



def generate_key(gpg, first_name, last_name = "localhost", domain= "localhost", passphrase=None):
    "Generate a key"
    params = {
        'Key-Type': 'RSA',
        'Key-Length': 1024,
        'Subkey-Type': 'RSA',
        'Subkey-Length': 2048,
        'Name-Comment': 'A test user',
        'Expire-Date': 0
}
    params['Name-Real'] = '%s %s' % (first_name, last_name)
    params['Name-Email'] = ("%s.%s@%s" % (first_name, last_name, domain)).lower()
#    if passphrase is None:
#        passphrase = ("%s%s" % (first_name[0], last_name)).lower()
#    params['Passphrase'] = passphrase
    cmd = gpg.gen_key_input(**params)
    return gpg.gen_key(cmd)


keys = [generate_key(theGpg, server) for server in servers]
for i in range(len(servers)):
    keyDictionary[servers[i]] = keys[i]
    print servers[i], ":", keys[i]

theFile = open("keyFile.key", "w")
for i in range(len(servers)):
    theFile.write(servers[i] + ":" + str(keys[i]) + "\n")

theFile.close()

###### END KEY_FILE_GENERATOR #####
