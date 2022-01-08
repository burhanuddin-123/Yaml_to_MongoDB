import pymongo

class Connection:
    def __init__(self):
        # Creating myclient object
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017")

        # Creating database object, if database is there it will get selected else will create the database.
        self.mydb = self.myclient["IPL_records"]

    def create_collection(self, name):
        self.mycollection = self.mydb[name]
    
    def insert_one_records(self, record):
        self.mycollection.insert_one(record)
    
    def insert_many_records(self, records_list):
        self.mycollection.insert_many(records_list)

