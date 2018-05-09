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
        table = soup.find(name ='table',attrs={'width':'99%'})
        tds = table.findAll(name ='td')
        for i in range(len(tds)):
            if i!=0:
                font = tds[i].find(name = 'a') 
                print(font.getText().strip('\n').replace(' ',''))
                self.fin.write(font.getText().strip('\n').replace(' ','').replace('\n','')+'\n')
                self.fin.write('null\n')
                self.fin.write('null\n')
                self.fin.write('null\n')
        self.fin.write('#藏品信息#\n')
        cli = self.obj.find_element_by_link_text('美育空间')
        cli.click()  
        self.fin.write('#教育信息#\n')
        soup = BeautifulSoup(self.obj.page_source,'html.parser')
        table = soup.find(name ='table',attrs={'width':'99%'})
        tds = table.findAll(name ='td')
        for i in range(len(tds)):
            if i!=0 and i!=len(tds)-1:
               # print(tds[i])
                atext = tds[i].find(name = 'a')
               # print(atext)
                font = atext.find('font')
                print(font)
if __name__ == '__main__':
    rep = Reptile("http://www.bhmdw.com/0zz_zhan/cj_zhan3/3lishutong/index.asp?id=lishutong&classid=10303&Page=1","李叔同故居纪念馆")
    rep.builddriver()
    rep.writeintxt()
    rep.exhibition()
    #rep.destroy()