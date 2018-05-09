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
                ul = soup.find(name = 'ul',attrs={'style':'display:inline-block'})
                print(ul)
                lis = ul.findAll(name = 'li')
                for li in lis:
                    span = li.find(name = 'span')
                    print(span.getText())
                    self.fin.write(span.getText()+'\n')
                    self.fin.write('null\n')
                    self.fin.write('null\n')
                    self.fin.write('null\n')
                cli = self.obj.find_element_by_link_text('[下一页]')
                cli.click()
                i = i+1
            except:
                break
        self.fin.write('#藏品信息#\n')
        cang = self.obj.find_element_by_link_text('精品典藏')
        cang.click()
        i = 0
        while i<8:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                ul = soup.find(name = 'ul',attrs={'class':'quality_list'})
                lis = ul.findAll(name = 'li')
                for li in lis:
                    span = li.find(name = 'span')
                    self.fin.write(span.getText()+'\n')
                    self.fin.write('null\n')
                    self.fin.write('null\n')
                cli = self.obj.find_element_by_link_text('[下一页]')
                cli.click()
                i=i+1      
            except:
                break
        self.fin.write('#教育信息#\n')
        cang = self.obj.find_element_by_link_text('公共教育')
        cang.click()
        i = 0
        while i<8:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                divs = soup.findAll(name = 'div',attrs= {'class':'listpictext_right'})
                for div in divs: 
                    span = div.find(name = 'span')
                    self.fin.write(span.getText()+'\n')
                    self.fin.write(div.getText().replace('%s'%span.getText(),'').replace(' ','').strip('\n')+'\n')
                    self.fin.write('null\n')
                    print(span.getText())
                    print(div.getText())
                cli = self.obj.find_element_by_link_text('[下一页]')
                cli.click()
                i=i+1      
            except:
                break
        self.fin.write('#学术信息#\n')
if __name__ == '__main__':
    rep = Reptile("http://www.tjbwg.com/ExhibitionList_10410.html","天津博物馆")
    rep.builddriver()
    rep.writeintxt()
    rep.exhibition()
    rep.destroy()