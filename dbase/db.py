import _mysql as mdb
import logging

# run a query on the database
def connect(self,query):
    # init variables
    dbinfo = self.config["database"]
    con = None
    cur = None
    result = None
    # establish connection, run query, return info
    try:
        con = mdb.connect(dbinfo["hostname"], dbinfo["username"], dbinfo["password"], dbinfo["database"])
        logging.debug("Running query: %s" % query)
        con.query(query)
        result = con.store_result().fetch_row(0)
    # return error if it fails
    except mdb.MySQLError, e:
        logging.debug("MySQL error %d: %s" % (e.args[0], e.args[1]))
    except AttributeError, e:
        logging.debug("AttributeError: %s" % (e.args[0]))
    # clean up
    finally:
        if con:
            con.close()
    return result