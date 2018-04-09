'''
Created on 2018年4月4日

@author: SBC
'''
from bs4 import BeautifulSoup
class HTMLParser(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def parHtml(self,html):
        soup = BeautifulSoup(html,'lxml')
        ret = []
        next_page = soup.find('a',attrs={'class':'next-page'})
        try:
            next_page_url = next_page['href']
        except:
            print('没有下一页了')
            next_page_url = None
        for tb in soup.find_all('table',attrs={'class': 'newlist'}):
#             print(tb.find('td'))
            dic = {}
            for td in tb.find_all('td'):
                try:
                    if td['class'] == ['zwmc']:
                        dic['position'] = td.text.strip()
                    if td['class'] == ['gsmc']:
                        dic['company'] = td.text.strip()
                    if td['class'] == ['zwyx']:
#                         dic['salary'] = td.text.strip()
                          salary = td.text.strip().split('-')
                          dic['low_salary'] = int(salary[0])
                          dic['high_salary'] = int(salary[1])
                          print('最低：'+ salary[0]+'  最高：'+salary[1])  
                    if td['class'] == ['gzdd']:
                        dic['gzdd'] = td.text.strip()
                except:
                    continue
            if next_page_url is not None:
                dic['next_page_url'] = next_page_url
            ret.append(dic)
        return ret