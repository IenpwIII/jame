import dbase.db
import terrain.terraingen
import settings

class MLoop():
    def run(self):
        self.config = settings.load(self,"jame.ini")
        query = "SELECT VERSION()"
        print "Version: %s" % dbase.db.connect(self,query)[0]

if __name__ == "__main__":
    a = MLoop()
    a.run()