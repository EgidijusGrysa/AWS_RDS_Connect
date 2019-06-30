class Instances():

    def __init__(self,name,isAvail,endpoint,port,dbuser,dbname):
        self.name = name
        self.isAvail = isAvail
        self.endpoint = endpoint
        self.port = port
        self.dbuser = dbuser
        self.dbname = dbname

# to string
    def __str__(self):
        return self.name + '\n' + self.isAvail + '\n' +self.endpoint + '\n' + str(self.port) + '\n' + self.dbuser + '\n' + self.dbname
            