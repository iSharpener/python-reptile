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
        i = 0
        while i<5:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                items = soup.findAll(name ='div',attrs={'class':'item'})
                for item in items:
                    name = item.find(name = 'a')
                    print(name.getText()+'\n')
                    self.fin.write(name.getText()+'\n')
                    clock = item.findAll(name = 'span')
                    self.fin.write(clock[1].getText()+'\n')
                    self.fin.write(clock[0].getText()+'\n')
                    self.fin.write('null\n')
                    print(clock[0].getText()+'\n')
                    print(clock[1].getText()+'\n')
                   # print(item)
                cli = self.obj.find_element_by_class_name('next')
                cli.click()
                i=i+1
            except:
                break
        self.fin.write('#藏品信息#\n')
        self.fin.write('#教育信息#\n')
        self.fin.write('#学术信息#\n')
if __name__ == '__main__':
    rep = Reptile("http://www.zgnybwg.com.cn/plan/zh/exhibition.html","中国农业博物馆")
    rep.builddriver()
    rep.writeintxt()
    rep.exhibition()
    rep.destroy()