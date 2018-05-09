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
        i =0
        while i<3:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                divs = soup.findAll(name = 'div',attrs={'class':'pro'})
                for div in divs:
                   # print(div)
                    name = div.find(name = 'a',attrs={'class':'proname'})
                    d = div.find(name ='div')
                    self.fin.write(name.getText()+'\n')
                    self.fin.write('null\n')
                    print(name.getText())
                    self.fin.write(d.getText()+'\n')
                    self.fin.write('null\n')
                    print(d.getText())
                next = self.obj.find_element_by_link_text('下一页')
                next.click()
                i = i+1
            except:
                break
        cang = self.obj.find_element_by_link_text('研究收藏')
        cang.click()
        jin = self.obj.find_element_by_link_text('馆藏珍品')
        jin.click()
        self.fin.write('#藏品信息#\n')
        i =0
        while i<3:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                ul = soup.find(name = 'ul',attrs={'class':'index_news'})
                lis = ul.findAll(name = 'li')
                for li in lis:
                    print(li)
                    name = li.find(name = 'a')
                    span = li.find(name = 'span')
                    print(name.getText())
                    self.fin.write(name.getText().replace('%s'%span.getText(),'')+'\n')
                    self.fin.write(span.getText()+'\n')
                    self.fin.write('null\n')
                    print(span.getText())
                next = self.obj.find_element_by_link_text('下一页')
                next.click()
                i = i+1
            except:
                break
        cang = self.obj.find_element_by_link_text('教育活动')
        cang.click()
        jin = self.obj.find_element_by_link_text('科普传播')
        jin.click()
        self.fin.write('#教育信息#\n')
        i=0
        while i<10:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                ul = soup.find(name = 'ul',attrs={'class':'index_news'})
                lis = ul.findAll(name = 'li')
                for li in lis:
                    name = li.find(name = 'a')
                    span = li.find(name = 'span')
                    print(name.getText())
                    self.fin.write(name.getText().replace('%s'%span.getText(),'')+'\n')
                    self.fin.write('null\n')
                    self.fin.write(span.getText()+'\n')
                    print(span.getText())
                next = self.obj.find_element_by_link_text('下一页')
                next.click()
                i = i+1
            except:
                break
        cang = self.obj.find_element_by_link_text('研究收藏')
        cang.click()
        jin = self.obj.find_element_by_link_text('学术动态')
        jin.click()
        self.fin.write('#学术信息#\n')
        i=0
        while i<5:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                ul = soup.find(name = 'ul',attrs={'class':'index_news'})
                lis = ul.findAll(name = 'li')
                for li in lis:
                    name = li.find(name = 'a')
                    span = li.find(name = 'span')
                    print(name.getText())
                    self.fin.write(name.getText().replace('%s'%span.getText(),'')+'\n')
                    self.fin.write('null\n')
                    self.fin.write(span.getText()+'\n')
                    print(span.getText())
                next = self.obj.find_element_by_link_text('下一页')
                next.click()
                i = i+1
            except:
                break
if __name__ == '__main__':
    rep = Reptile("http://www.tjnhm.com/index.php?p=zlxx&lanmu=2&page=1","天津自然博物馆")
    rep.builddriver()
    rep.writeintxt()
    rep.exhibition()
    rep.destroy()