'''
Created on 2018年4月4日

@author: SBC
'''
import urllib3
import requests
class HTMLDownloader(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def downloadUrl(self,url):
        # 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
        http = urllib3.PoolManager()
        # 通过request()方法创建一个请求：
        r = http.request('GET', url)
        if r.status != 200 :
            return False
        else:
            return r.data.decode()
        