'''
Created on 2018年3月23日

@author: Xiaopeng
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import re
class Reptile:
    def __init__(self,url,museum):
        self.wholeurl = url
        self.museum = museum
    def builddriver(self):
        obj = webdriver.Chrome("/Users/xiaopeng/Downloads/chromedriver") #加载网址
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
    def exhibition(self):
        self.fin.write('#展览信息#\n')
        i = 0
        while i<2:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                lists = soup.findAll('div',attrs={'class','list_cl r'})
                for list in lists:
                    name = list.find(name = 'a',attrs={'target':'_blank'})
                    dd = list.find(name ='dd')
                    self.fin.write(name.getText()+'\n')
                    print(name.getText())
                    self.fin.write('null\n')
                    self.fin.write('null\n')
                    if dd.getText().strip()=='':
                        self.fin.write('null\n')
                    else:
                        self.fin.write(dd.getText().strip()+'\n')
                    print(dd.getText().strip())  
                              
                ele = self.obj.find_element_by_link_text('末页')
                ele.click()
            except:
                break
        self.fin.write('#藏品信息#\n')
        education = self.obj.find_element_by_xpath('//*[@id="Map"]/area[6]')
        print(education)
        education.click()
        print(self.obj.page_source)
        j=0
        soup = BeautifulSoup(self.obj.page_source,'html.parser')
        while i<2:
            try:
                dds = soup.findAll(name='dd')
                for ddt in dds:
                    ass = ddt.find(name ='a')
                    self.fin.write(ass.getText()+'\n')
                    self.fin.write('null\n')
                    self.fin.write('null\n')
                    print(ass)
                next = self.obj.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div/li[5]/a')
                next.click()
                i=i+1
                
            except:
                break
        self.fin.write('#教育信息#\n')
        education = self.obj.find_element_by_xpath('//*[@id="Map"]/area[7]')
        education.click()
        soup = BeautifulSoup(self.obj.page_source,'html.parser')
        lls = soup.findAll(name ='div',attrs={'class':'list_l l'})
        for ll in lls:
            da = ll.find(name ='a',attrs={'target':'_blank'})
            span = ll.find(name ='span',attrs={'class':'time'})
            print(da.getText())
            self.fin.write(da.getText()+'\n')
            self.fin.write('null\n')
            print(span.getText())
            self.fin.write(span.getText()+'\n')
        self.fin.write('#学术信息#\n')
        xueshu = self.obj.find_element_by_xpath('//*[@id="Map"]/area[5]')
        xueshu.click()
        soup = BeautifulSoup(self.obj.page_source,'html.parser')
        lls = soup.findAll(name ='div',attrs={'class':'list_l l'})
        for ll in lls:
            da = ll.find(name ='a',attrs={'target':'_blank'})
            span = ll.find(name ='span',attrs={'class':'time'})
            print(da.getText())
            self.fin.write(da.getText()+'\n')
            print(span.getText())
            self.fin.write('null\n')
            self.fin.write(span.getText()+'\n')
if __name__ == '__main__':
    rep = Reptile('http://www.luxunmuseum.com.cn/a/zhanlan/zhanlanhuigu/','北京鲁迅博物馆')
    rep.builddriver()
    rep.writeintxt()
    rep.exhibition()
    rep.destroy()