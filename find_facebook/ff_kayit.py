from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys


## process for disablle browser notification 
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chrome_options=chrome_options)

time.sleep(5)

browser.get("https://www.facebook.com/")

time.sleep(5)

kullanici = browser.find_element_by_name("email")
sifre = browser.find_element_by_name("pass")
kullanici.send_keys("demirmigferdibi@gmail.com")
sifre.send_keys("sallamacay54")

time.sleep(3)

giris = browser.find_element_by_id("loginbutton")
giris.click()

time.sleep(10)

arama=browser.find_element_by_name("q")
arama.send_keys("classic book")
button_search = browser.find_element_by_class_name("_585_")
button_search.click()

time.sleep(10)
print("*****************************************************")
button_group = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[8]")
button_group.click()

time.sleep(10)
buttons =  browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/span/div/div/div[2]/div/a[2]")
buttons.click()

time.sleep(4)
c="1"
#grup1 = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[1]/div["+ c +"]/div/div/div[2]/div/div[1]/div[1]/div/div/div/a")
#grup1.click()

body = browser.find_element_by_tag_name("body")

a=[]
b=[]
for i in range(1,3):

    following = browser.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[1]/div[*]/div/div/div[2]/div/div[1]/div[1]/div/div/div/a")
    for j in following:
        print(j.text)
        print("*********************************************************************")
        print(j.get_attribute('href'))
        a.append(j.text)
        b.append(j.get_attribute('href'))
        
    print(i)
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(5)

#df = pd.DataFrame(data=a)
s=list(set(a))
df2 = pd.DataFrame(data=s)

ss=list(set(b))
bb = pd.DataFrame(data=ss)

print(b[2])

#print(s)

print("111111111111111111111111111111111111111")

def viewFull(a):
    following = browser.find_elements_by_xpath(a)
    return a



d=[]
for i in b:
    browser.get(i)
    time.sleep(5)
    boby = browser.find_element_by_tag_name("body")
    dollowing = browser.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[*]/div/div[2]/div[1]/div[2]/div[2]/div")   
    for i in range(5):
        try:
            boby.send_keys(Keys.PAGE_DOWN)
            time.sleep(5) 
            dollowing = browser.find_elements_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[*]/div/div[2]/div[1]/div[2]/div[2]/div")
            print(dollowing[i].text)
            d.append(dollowing[i].text)        
        except:
            pass
        
        

