def createTile(tiletype,x,y,z):
	query = _mysql.escape_string("INSERT INTO `tiles` (`x`,`y`,`z`) VALUES (%s,%s,%s)" %(x,y,z))