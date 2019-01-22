# -*- coding:utf-8 -*-
import os
import ConfigParser

def Getmodulekey(config_path,keys,values):
    if os.path.exists(config_path):
        config = ConfigParser.ConfigParser()
        config.read(config_path)
        value = config.get(keys,values)
        return value
    else:
        print "Not Found Config"