'''
Created on 2018年3月16日

@author: Xiaopeng
'''
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#dcap = dict(DesiredCapabilities.CHROME)  #设置userAgent
#dcap["chrome.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
class exhibition:
    def __init__(self,museum,status,topic,time,place,introduction):
        self.topic = topic
        self.time = time
        self.status = status
        self.place = place
        self.introduction = introduction
        self.museum = museum
    def setMuseum(self,museum):
        self.museum = museum
class Reptile:
    def __init__(self,url,museum):
        self.wholeurl = url
        self.museum = museum
    def builddriver(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs);
        #obj = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\chromedriver.exe') #加载网址
        obj = webdriver.Chrome(executable_path='/Users/xiaopeng/Downloads/chromedriver',chrome_options=chrome_options) #加载网址
        print("浏览器最大化")
        obj.maximize_window()
        obj.get(self.wholeurl)
        obj.save_screenshot('%s.png'%self.museum)   #截图保存
        self.obj = obj
    def writeintxt(self):
        fin = open('%s.txt'%self.museum,'w',encoding='utf-8')
        self.fin = fin
    def destroy(self):
        self.fin.close()
        self.obj.quit()
    #爬取展览信息
    def exhibition(self):
        i = 1
        self.fin.write("#展览信息#\n")
        while True:
            try:
                soup = BeautifulSoup(self.obj.page_source.encode('utf-8'),'html.parser')
                print(soup.title)
                print('正在处理第%d页的展览信息'%i)
                div = soup.find(name='div',attrs={'class':'table'})
                #print(div)
                table = div.find(name='table')
                for tr in table.findAll(name='tr'):
                    #print(len(tr))
                    j = 1
                    tds = tr.findAll(name = 'td')
                    #status = tds[0].find(name ='span').getText()
                    for td in tds:
                        if j==1:
                            if td.find(name = 'a').getText()!='':
                                self.fin.write(td.find(name = 'a').getText()+'\n')
                            else:
                                self.fin.write('null\n')
                        if j==2:
                            self.fin.write(td.getText().strip('\n')+"\n")
                            print(td.getText())
                        if j==3:
                            if((td.find(name ='span').getText())==''):                             
                                self.fin.write("null\n")
                                self.fin.write('null\n')
                                print("无时间详情")                               
                            else:
                                timeall = td.find(name='span').getText().strip('\n').replace(' ','')                            
                                self.fin.write(timeall+'\n')
                                self.fin.write('null\n')
            
                                #print(td.find(name ='span').getText().replace(' ',''))
                        #print(td.getText())
                        j = j+1
                f = self.obj.find_element_by_xpath('//*[@id="temporary2"]/div/div[2]/a[5]')
                f.click();
                print("\n\n\n")
                i = i+1
            except Exception as e:
                print(e)
                break
    def Other(self):
        self.fin.write("#藏品信息#\n")
        #爬取教育信息
        self.fin.write("#教育信息#\n")
        f = self.obj.find_element_by_link_text('教育')
        print("教育标签")
        print(f)
        f.click()
        #print(self.obj.page_source)
        soup = BeautifulSoup(self.obj.page_source.encode('utf-8'),'html.parser')
        containdivs =soup.findAll(name='div',attrs={'class':re.compile('.*?clearfix.*?')})
        for div in containdivs[0:len(containdivs)-1]:
            text = div.find(name='div',attrs={'class':'text'})
            h = text.find(name ='h2')
            ps = text.findAll(name = 'p')
            print(h.getText())
            if h.getText()!='':
                self.fin.write(h.getText()+"\n")
            else:
                self.fin.write('null\n')
            if ps[2].getText()!='':
                self.fin.write(ps[2].getText()+"\n")
            else:
                 self.fin.write('null\n')
            self.fin.write('null\n')
        print('\n')
        #爬取学术活动
        self.fin.write("#学术信息#\n")
        study = self.obj.find_element_by_link_text('学术')
        study.click()
        study1 = self.obj.find_element_by_link_text('学术活动')
        study1.click()
        num = self.obj.window_handles
        self.obj.switch_to_window(num[1])
        page = 0
        while page<5:
            soup1 = BeautifulSoup(self.obj.page_source.encode('utf-8'),'html.parser')
            listdiv = soup1.find(name = 'div',attrs={'id':'lists'}) 
            lis = listdiv.findAll(name='li')
            for li in lis:
                atext = li.find(name = 'a')
                aspan = li.find(name = 'span')
                if atext.getText()!='':
                   self.fin.write(atext.getText()+"\n")
                else:
                    self.fin.write('null\n')
                self.fin.write('null\n')
                if aspan.getText()!='':
                    self.fin.write(aspan.getText().replace(' ','')+"\n")
                else:
                    self.fin.write('null\n')
                print(aspan.getText())
                print(atext.getText())
           
            time.sleep(2)
            atag = self.obj.find_element_by_id('next')
            atag.click()
            page = page+1
rep = Reptile("http://www.dpm.org.cn/shows.html","故宫博物院")
rep.builddriver()
rep.writeintxt()
rep.exhibition()
rep.Other()
rep.destroy()
        
