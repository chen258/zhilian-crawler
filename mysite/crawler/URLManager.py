'''
Created on 2018年4月4日

@author: SBC
'''

class URLManager(object):
    '''
    classdocs
    '''
    url_list = []
    url_his_list = []

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def haveUrlValue(self):
        '''
        judge urllist is null?
        '''
        return len(self.url_list)
    
    def addUrl(self,url):
        if self.url_his_list.count(url) :
           print('已经有过这个url了，不去添加了'+url)
        else:
            self.url_list.append(url)
            self.url_his_list.append(url)
            print('添加这个url到管理器中'+url)
             
    def rmUrl(self,url):
        if self.url_list.count(url) :
            self.url_list.remove(url)
            print('url_list中移除这个值'+url)
        else:
            print('url管理器中没有这个值，无法移除：'+url)
    
    def popUrl(self):
        '''
        移除栈顶的url
        '''
        return self.url_list.pop(0)