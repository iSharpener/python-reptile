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
    def destroy(self):
        self.fin.close()
        self.obj.quit()
    def exhibition(self):
        self.fin.write('#展览信息#\n')
        soup = BeautifulSoup(self.obj.page_source,'html.parser')
        print(soup)
        divs = soup.findAll(name = 'div',attrs={'class':'show-column'})
        for div in divs:
            lis = div.findAll(name = 'li')
            for b in lis:
                a = b.find(name = 'a')
                em = b.find(name ='em')
                self.fin.write(a.getText()+'\n')
                print(a.getText())
                self.fin.write('null\n')
                self.fin.write(em.getText()+'\n')
                self.fin.write('null\n')
                print(em.getText())  
        self.fin.write('#藏品信息#\n')
        self.fin.write('#教育信息#\n')
        self.fin.write('#学术信息#\n')
if __name__ == '__main__':
    rep = Reptile("http://www.bmnh.org.cn/Html/List/list10.html","北京自然博物馆")
    rep.builddriver()
    rep.writeintxt()
    rep.exhibition()
    rep.destroy()