import ConfigParser

#load a config file
def load(self,cfile):
    dict1 = {}
    config = ConfigParser.ConfigParser()
    config.read(cfile)
    sections = config.sections()
    for i in sections:
        dict1[i] = sectionMap(self,config,i)
    return dict1

#load a section from the config file
def sectionMap(self,config,section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1