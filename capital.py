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
        print(self.obj.page_source)
#         while True:
        try:
            soup = BeautifulSoup(self.obj.page_source,'html.parser')
            tds = soup.findAll(name = 'td',attrs={'align':'center'})
            for td in tds:
                print(td)
        except:
            pass
#                 break
if __name__ == '__main__':
    rep = Reptile("http://www.capitalmuseum.org.cn/zlxx/zlhf.htm","首都博物馆")
    rep.builddriver()
    rep.writeintxt()
    rep.exhibition()
    rep.destroy()