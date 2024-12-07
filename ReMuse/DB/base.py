from tinydb import TinyDB
import os

class BaseDB:
    db = None

    def __init__(self):
        self.db = TinyDB(os.getcwd()+'/ReMuse/data/'+self.table+'.json')
