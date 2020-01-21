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
        
        

    




"""
//*[@id="u_ps_fetchstream_10_3_2"]/div/div[2]/div/div[1]/div[1]/div/div/div/a
//*[@id="u_ps_fetchstream_10_3_4"]/div/div[2]/div/div[1]/div[1]/div/div/div/a
/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div[1]/div/div/div/a
//*[@id="u_ps_fetchstream_10_3_6"]/div/div[2]/div/div[1]/div[1]/div/div/div/a
/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/div/div/a

/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div[2]/div/div[1]/div[1]/div/div/div/a
/html/body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[2]/div/div/div/div[1]/div[*]/div/div/div[2]/div/div[1]/div[1]/div/div/div/a

/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[*]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div/p/text()
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[5]/div/div[2]/div[1]/div[2]/div[2]/div/p/text()[1]
/html/body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[8]

//*[@id="js_nr"]/div/div[2]/div/a[2]
//*[@id="js_4o"]/div/div[2]/div/a[2]
//*[@id="js_69"]/div/div[2]/div/a[2]
//*[@id="js_49"]/div/div[2]/div/a[2]
/html/body/div[1]/div[3]/div[1]/div/div[3]/div[1]/div/div/div/span/div/div/div[2]/div/a[2]


document.querySelector("#js_6 > div > div:nth-child(2) > div > a:nth-child(3) > span")


//*[@id="js_6"]/div/div[2]/div/a[2]/span


#js_f5 > div > div:nth-child(2) > div > a:nth-child(3)
//*[@id="js_yo"]/div/div[2]/div/a[2]/span



//*[@id='js_1g']/div/div[2]/div/a[2]/label
//*[@id="js_1i"]/div/div[2]/div/a[2]
//*[@id="js_66"]/div/div[2]/div/a[2]/span
//*[@id="js_7"]/div/div[2]/div/a[2]/span
//*[@id="js_7"]/div/div[2]/div/a[2]/span
//*[@id="js_2f"]/div/div[2]/div/a[2]/span
//*[@id="js_kp"]/div/div[2]/div/a[2]/span


<span class="_6ed5">Herkese Açık gruplar</span>


<span class="_6ed5">Herkese Açık gruplar</span>










/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]





/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[2]
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[2]
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[8]/div/div[2]/div[1]/div[2]/div[2]/div/p/text()


/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]

/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[1]/div[5]/div/div[2]/div[1]/div[2]/div[2]
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[2]
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[2]
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]


/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[2]
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[2]/div
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[2]
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]


/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[20]
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[19]
"""




"""

/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[21]/div/div[2]/div[1]/div[2]/div[2]/div
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[12]/div/div[2]/div[1]/div[2]/div[2]/div
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[2]/div


"""

"""
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[4]/div/div[2]/div[1]/div[2]/div[2]/div
"""
"""
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[16]/div/div[2]/div[1]/div[2]/div[2]/div
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[16]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[16]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[16]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div/span

/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[18]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div
/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[5]/div[4]/div/div[1]/div[18]/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/span[1]
"""
