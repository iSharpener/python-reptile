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
        div = soup.find(name = 'div',attrs={'class':'basicList'})
        lis = div.findAll(name = 'li')
        for li in lis:
            #print(li)
            di = li.find(name = 'div',attrs ={'class':'basicDes'})
            name = di.find(name = 'h3')
            introduction = di.find(name = 'p')
            self.fin.write(name.getText()+'\n')
            self.fin.write('null\n')
            self.fin.write('null\n')
            print(introduction)
            self.fin.write(introduction.getText()+'\n')
        cang = self.obj.find_element_by_link_text('馆藏文物')
        cang.click()
        cang = self.obj.find_element_by_link_text('古近代文物')
        cang.click()
        i = 0
        while i<3:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                div = soup.find(name = 'div',attrs={'class':'relicAppRight'})
                print(div)
                i=i+1
            except:
                break 
if __name__ == '__main__':
    rep = Reptile("http://www.jb.mil.cn/zlcl/jbcl/","中国人民革命军事博物馆")
    rep.builddriver()
    rep.writeintxt()
    rep.exhibition()
   # rep.destroy()