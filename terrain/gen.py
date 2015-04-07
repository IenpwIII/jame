import logging

import dbase

terrainTypes = {
    "grass":{"name":"grass","movecost":1,"defence":1,"id":1},
}

# insert a tile and the necessary info into the db
def createTile(self,tiletype,x,y,z):
    #prepare and execute the creation query
    createquery = "INSERT INTO `tiles` (`x`,`y`,`z`) VALUES (%s,%s,%s);" %(x,y,z)
    dbase.db.connect(self,createquery)
    #retreive the id of the tile just inserted
    idquery = "SELECT `id` FROM `tiles` WHERE `x`=%s AND `y`=%s AND `z`=%s;" %(x,y,z)
    tileid = dbase.db.connect(self,idquery)[0][0]
    logging.debug(tileid)
    #store the tiletype as contents
    typequery = "INSERT INTO `tilecontents` (`objid`,`objtable`,`tileid`) VALUES (%s,\'terraintypes\',%s);" % (terrainTypes[tiletype]["id"],tileid)
    dbase.db.connect(self,typequery)