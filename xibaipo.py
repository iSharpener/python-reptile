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
        self.fin.write('#藏品信息#\n')
        i = 0
        while i<4:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                ul = soup.find(name = 'ul',attrs={'class':'piclist'})
                lis = ul.findAll(name = 'li')
                for li in lis:
                    #print(li)
                    h2 = li.find(name = 'h2')
                    self.fin.write(h2.getText()+'\n')
                    self.fin.write('null\n')
                    self.fin.write('null\n')
                cli = self.obj.find_element_by_link_text('下页')
                cli.click()
                i+=1  
            except:
                break
        self.fin.write('#教育信息#\n')
        cli = self.obj.find_element_by_link_text('文博天地')
        cli.click()
        soup = BeautifulSoup(self.obj.page_source,'html.parser')
        div = soup.find(name = 'div',attrs={'class':'all-content'})
        h2s = div.findAll(name = 'h2')
        for h2 in h2s:
            atext = h2.find(name = 'a')
            dtext = h2.find(name = 'div',attrs={'class':'rt'})
           # print(atext.getText())
            self.fin.write(atext.getText()+'\n')
            self.fin.write('null\n')
            self.fin.write(dtext.getText()+'\n')
            #print(dtext.getText())
        self.fin.write('#学术信息#\n')
        cli = self.obj.find_element_by_link_text('学术长廊')
        cli.click()
        soup = BeautifulSoup(self.obj.page_source,'html.parser')
        print(soup)
        div = soup.find(name = 'div',attrs={'class':'zygg'})
        print(div)
        h2s = div.findAll(name = 'h2')
        for h2 in h2s:
            print(h2)


if __name__ == '__main__':
    rep = Reptile("http://www.xbpjng.cn/wenbotiandi/wenwu.aspx","西柏坡纪念馆")
    rep.builddriver()
    rep.writeintxt()
    rep.exhibition()
   # rep.destroy()