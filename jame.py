import logging
import random

import dbase.db
import terrain.gen
import settings

class MLoop():
    def initLog(self):
        logging.basicConfig(filename='debug.log',level=logging.DEBUG)
    def run(self):
        self.config = settings.load(self,"jame.ini")
        query = "SELECT VERSION()"
        print "MySQL version: %s" % dbase.db.connect(self,query)[0]
        for i in xrange(-9,9):
            for j in xrange(-9,9):
                terrain.gen.createTile(self,"grass",i,j,0)

if __name__ == "__main__":
    a = MLoop()
    a.initLog()
    a.run()