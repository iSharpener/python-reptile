'''
Created on 2018年3月22日

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
        obj = webdriver.Chrome(executable_path='E:\安装包\chromedriver_win32\chromedriver.exe') #加载网址
        print("浏览器最大化")
        obj.maximize_window()
        obj.get(self.wholeurl)
        obj.save_screenshot('%s.png'%self.museum)   #截图保存
        self.obj = obj
    def writeintxt(self):
        fin = open('%s.txt'%self.museum,'w',encoding='utf-8')
        self.fin = fin
    def exhibition(self):
        soup = BeautifulSoup(self.obj.page_source,'html.parser')
        zhanlans = soup.findAll(name='li', attrs={'target':'_blank'})
        for zhanlan in zhanlans:
            print(zhanlan)
            name = zhanlan.find(name='span',attrs={'class':'title'})
            # showtime = zhanlan.find(name = 'span',attrs={'class':re.compile('.*?Preview')})
            print(name)
            #print(showtime.getText())
    def destroy(self):
        self.fin.close()
        self.obj.quit()
if __name__ == '__main__':
    rep = Reptile('http://www.chnmuseum.cn/tabid/230/Default.aspx','中国国家博物馆')
    rep.builddriver()
    rep.writeintxt()
    rep.exhibition()
    rep.destroy()
    