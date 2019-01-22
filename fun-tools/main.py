# -*- coding:utf-8 -*-
import os
import argparse
import lib.readconfig
from lib.checkcms import whatcms


code_logo = """
███████╗██╗   ██╗███╗   ██╗   ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔════╝██║   ██║████╗  ██║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
█████╗  ██║   ██║██╔██╗ ██║█████╗██║   ██║   ██║██║   ██║██║     ███████╗
██╔══╝  ██║   ██║██║╚██╗██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
██║     ╚██████╔╝██║ ╚████║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝      ╚═════╝ ╚═╝  ╚═══╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                                       
"""
def setpath(rootpath):
    Fun_Root_Path = rootpath
    Fun_Plugin_Path = os.path.join(Fun_Root_Path,"plugins")

def Checkcms(maxsize):
    url = raw_input(">>>>> ")
    g = whatcms(url,maxsize)
    g.whatweb()




def main():
    print code_logo
    setpath(os.getcwd())
    parser = argparse.ArgumentParser(description="How to Use this scrpit")
    parser.add_argument("--u",metavar="url",help="--u https://xxx.xx")
    args = parser.parse_args()
    try:
        maxsize = lib.readconfig.Getmodulekey(os.path.join(os.getcwd(),"config.conf"),'CMS','maxsize')
        Checkcms(maxsize)
    except Exception,e:
        print e


if __name__ == "__main__":
    main()