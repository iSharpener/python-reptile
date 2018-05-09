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
        self.fin.write('<-----展览信息----->\n')
        soup = BeautifulSoup(self.obj.page_source,'html.parser')
        lis = soup.findAll(name = 'li',attrs={'style':' text-align:left'})
        for li in lis:
            contain = li.find(name = 'a')
            print(contain.getText()+'\n')
            self.fin.write(contain.getText()+'\n')
            self.fin.write('null\n')
            self.fin.write('null\n')
            self.fin.write('null\n')
        cang = self.obj.find_element_by_link_text('馆藏精品')
        cang.click()
        self.fin.write('#藏品信息#\n')
        while True:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                div = soup.find(name = 'div',attrs={'class':'jpPic'})
                ul = div.find(name = 'ul')
                spans = ul.findAll(name = 'span')
                for span in spans:
                    print(span.getText())
                    self.fin.write(span.getText()+'\n')
                    self.fin.write('null\n')
                    self.fin.write('null\n')
                cli = self.obj.find_element_by_link_text('下页')
                if cli.get_attribute('disabled')=='true':
                    break
                cli.click()
            except:
                break
        keyan = self.obj.find_element_by_link_text('科研科普')
        keyan.click()
        yuandi = self.obj.find_element_by_link_text('科普园地')
        yuandi.click()
        self.fin.write('#教育信息#\n')
        self.fin.write('#学术信息#\n')
        i=0
        while i<5:
            try: 
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                div = soup.find(name = 'div',attrs={'class':'list'})
                ul = div.find(name = 'ul')
                lis = ul.findAll('li')
                for li in lis:
                    name = li.find(name = 'a')
                    clock = li.find(name='span')
                    print(name.getText())
                    self.fin.write(name.getText()+'\n')
                    print(clock.getText( ))
                    self.fin.write('null\n')
                    self.fin.write(clock.getText()+'\n')
                cli = self.obj.find_element_by_link_text('下页')
                cli.click()
                i=i+1
            except:
                break
            
if __name__ == '__main__':
    rep = Reptile("http://www.gmc.org.cn/hall/1/","中国地质博物馆")
    rep.builddriver()
    rep.writeintxt()
    rep.exhibition()
    rep.destroy()