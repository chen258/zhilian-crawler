'''
Created on 2018骞�4鏈�4鏃�

@author: SBC
'''
# from mysite import URLManager
# from mysite import HTMLDownloader
# from mysite import HTMLParser
# from mysite import DataCollect
from . import URLManager, HTMLDownloader, HTMLParser, DataCollect

class SpiderMan:
    '''
    classdocs
    '''
    url = ''
    urlm = URLManager.URLManager()
    html_down = HTMLDownloader.HTMLDownloader()
    html_par = HTMLParser.HTMLParser()
    dc = DataCollect.DataCollect()
    def __init__(self,url):
        '''
        Constructor
        '''
        print('spider init')
        self.url = url
        return
    
    def startSpider(self,file_name,res_name,keyword):
        '''
        StartDoSomething
        '''
        print('开启写信息')
        self.urlm.addUrl(self.url)
        tmp = 6;
        while   self.urlm.haveUrlValue() :
            if tmp <= 0:
                break
            #鍟�
            need_par_url = self.urlm.popUrl()
            need_par_html = self.html_down.downloadUrl(need_par_url)
            par_value = self.html_par.parHtml(need_par_html)
            try:
                if par_value[0]['next_page_url'] is not None :
                    self.urlm.addUrl(par_value[0]['next_page_url'])
            except:
                print('出错')  
            self.dc.saveData(par_value,file_name,keyword)
            tmp-=1
        self.dc.writeResult(keyword)            
        pass
    
