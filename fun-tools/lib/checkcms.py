# -*- coding:utf-8 -*-
import os
import sys
import json
import time
import gevent
import hashlib
import requests
from gevent import monkey
from gevent.queue import Queue

class whatcms:
    def __init__(self,url,maxsize):
        self.scan_url = url
        self.maxsize = maxsize
        print self.scan_url,self.maxsize
        self.tasks = Queue()
        fp = open(os.path.join(os.getcwd(),"poc/cmsinfo/cms.json"))
        cmsdata = json.load(fp,encoding='utf-8')
        for i in cmsdata:
            self.tasks.put(i)
        fp.close()
        print "cmsdata total:%d" %len(cmsdata)
    def md5(self,body):
        m2 = hashlib.md5()
        m2.update(body.encode('utf-8'))
        return m2.hexdigest()

    def clearqueue(slef):
        while not slef.tasks.empty():
            slef.tasks.get()
    
    def worker(self):
        data = self.tasks.get()
        test_url = self.scan_url+ data["url"]
        rtext = ''
        try:
            r = requests.get(test_url,timeout=10)
            if r.status_code != 200:
                return
            rtext = r.text
            print r
            if rtext is None:
                return
        except Exception,e:
            rtext = ''
        
        if data['re']:
            if rtext.find(data['re']) != -1:
                result = data['name']
                print "CMS:%s  Judge:%s re:%s"  %result,test_url,data['re']
                self.clearqueue()
                return True
        else:
            md5 = self.md5(rtext)
            if md5 == data['md5']:
                result = data['name']
                print "CMS:%s Judge:%s re:%s" %result,test_url,data['md5']
                self.clearqueue()
                return True

    def boss(self):
        while not self.tasks.empty():
            self.worker()
        
    def whatweb(self):
        start = time.clock()
        allr = [gevent.spawn(self.boss) for i in range(int(self.maxsize))]
        gevent.joinall(allr)
        end = time.clock()
        # print "cost: %f s" % end-start
