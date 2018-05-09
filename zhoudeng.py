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
                divs = soup.find(name = 'div',attrs={'class':'exhibits'})
                exps = divs.findAll(name = 'div',attrs={'class':'right_exhibits'})
                for exp in exps:
                    exp1 = exp.find(name = 'div',attrs={'class':'right_exhibits01'})
                    exp2 = exp.find(name = 'div',attrs={'class':'right_exhibits02'})
                    exp3 = exp.find(name = 'div',attrs={'class':'right_exhibits03'})
                    self.fin.write(exp1.getText()+'\n')
                    self.fin.write(exp2.getText()+'\n')
                    self.fin.write('null\n')
                    if exp3.getText()=='':
                        self.fin.write('null\n')
                    else:
                        self.fin.write(exp3.getText().replace('\n','')+'\n')
                cli = self.obj.find_element_by_link_text('下一页')
                cli.click()
                i+=1
            except:
                break
        cli = self.obj.find_element_by_link_text('文物鉴赏')
        cli.click()
        self.fin.write('#藏品信息#\n')
        i = 0
        while i<3:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                div = soup.find(name = 'div',attrs={'class':'relics'})
                ul = div.find(name ='ul')
                #print(ul)
                lis = ul.findAll(name = 'li',attrs={})
                #print(lis)
                for li in lis:
                    #print(li)
                    ps = li.find(name='p')
                    #print(ps)
                    self.fin.write(ps.getText()+'\n')
                    self.fin.write('null\n')
                    self.fin.write('null\n')
                cli = self.obj.find_element_by_link_text('下一页')
                cli.click()
                i+=1
            except:
                break
        self.fin.write('#教育信息#\n')
        cli = self.obj.find_element_by_link_text('教育园地')
        cli.click()
        cli = self.obj.find_element_by_link_text('社会活动')
        cli.click()
        i = 0
        while i<3:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                news = soup.find(name = 'div',attrs={'class':'news'})
                lis = news.findAll(name = 'li')
                for li in lis:
                #    print(li)
                    span = li.find(name = 'span')
                    ps = li.find(name = 'p')
                    self.fin.write(ps.getText()+'\n')
                    self.fin.write('null\n')
                    self.fin.write(span.getText()+'\n')
                cli = self.obj.find_element_by_link_text('下一页')
                cli.click()
                i+=1
            except:
                break
        self.fin.write('#学术信息#\n')
        cli = self.obj.find_element_by_link_text('学术研究')
        cli.click()
        i = 0
        while i<3:
            try:
                soup = BeautifulSoup(self.obj.page_source,'html.parser')
                news = soup.find(name = 'div',attrs={'class':'news'})
                lis = news.findAll(name = 'li')
                for li in lis:
                    print(li)
                    ps = li.find(name = 'p')
                    span = li.find(name = 'span')
                    self.fin.write(ps.getText()+'\n')
                    self.fin.write('null\n')
                    self.fin.write(span.getText()+'\n')
                cli = self.obj.find_element_by_link_text('下一页')
                cli.click()
                i+=1
            except:
                break
if __name__ == '__main__':
    rep = Reptile("http://www.mzhoudeng.com/exhibits.aspx?cateid=88","周恩来邓颖超纪念馆")
    rep.builddriver()
    rep.writeintxt()
    rep.exhibition()
    rep.destroy()