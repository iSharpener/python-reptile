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
        div = soup.find(name = 'div',attrs={'class':'zlhg_list'})
        lis = div.findAll(name ='li')
        for li in lis:
            span = li.find(name ='span')
            a = li.find(name ='a')
            self.fin.write(a.getText()+'\n')
            self.fin.write('null\n')
            self.fin.write(span.getText().replace('[','').replace(']','')+'\n')
            self.fin.write('null\n')
            print(a.getText())
            print(span.getText())
        self.fin.write('#藏品信息#\n')
        self.fin.write('#教育信息#\n')
        x = self.obj.find_element_by_link_text('科普园地')
        x.click()
        y = self.obj.find_element_by_link_text('发掘周口店')
        y.click()
        i=0
        while i<3:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                div = soup.find(name = 'div',attrs={'class':'zlhg_list'})
                lis = div.findAll(name ='li')
                for li in lis:
                    span = li.find(name ='span')
                    a = li.find(name ='a')
                    self.fin.write(a.getText()+'\n')
                    self.fin.write('null\n')
                    self.fin.write(span.getText().replace('[','').replace(']','')+'\n')
                    print(a.getText())
                    print(span.getText())
                m = self.obj.find_element_by_link_text('下一页')
                m.click()
                i=i+1
            except:
                break
        x = self.obj.find_element_by_link_text('学术研究')
        x.click()
        y = self.obj.find_element_by_link_text('科学研究')
        y.click()
        self.fin.write('#学术信息#\n')
        j=0
        while j<2:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                div = soup.find(name = 'div',attrs={'class':'zlhg2_list'})
                lis = div.findAll(name ='li')
                for li in lis:
                    span = li.find(name ='span')
                    a = li.find(name ='a')
                    self.fin.write(a.getText()+'\n')
                    self.fin.write('null\n')
                    self.fin.write(span.getText().replace('[','').replace(']','')+'\n')
                    print(a.getText())
                    print(span.getText())
                m = self.obj.find_element_by_link_text('下一页')
                m.click()
                j=j+1
            except:
                break
        
if __name__ == '__main__':
    rep = Reptile("http://www.zkd.cn/zlhg/index.jhtml","周口店北京人遗址博物馆")
    rep.builddriver()
    rep.writeintxt()
    rep.exhibition()
    rep.destroy()