import _mysql as mdb

# run a query on the database
def connect(self,query):
    # init variables
    dbinfo = self.config["database"]
    con = None
    cur = None
    result = None
    # establish connection, return info
    try:
        con = mdb.connect(dbinfo["hostname"], dbinfo["username"], dbinfo["password"], dbinfo["database"])
        con.query(query)
        result = con.store_result().fetch_row(0)
    # return error if it fails
    except mdb.MySQLError, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
    # clean up
    finally:
        if con:
            con.close()
    return result