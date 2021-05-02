import requests
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from check_scraper import Data_extract




driver = webdriver.Chrome()
sleep(3)
driver.maximize_window()
sleep(3)
driver.get("https://www.linkedin.com/")



sleep(10)

cookies_dict = {}
for cookie in driver.get_cookies():
    cookies_dict[cookie["name"]] = cookie["value"]

driver.close()

sleep(5)



resp = requests.get("https://www.linkedin.com/in/priyam-rao-15802915b/",
                   cookies = cookies_dict,
                   headers = {'user-agent':'Mozilla/5.0 (windows 10.0; win64; x64) Applewebkit',
                   'accept':'text/html,application/xhtml+xml,application/xml:q=0.0,ima',
                   'accept-encoding':'gzip,deflate,br',
                   'accept-language':'en-US,en;q=0.9',
                   'upgrade-insecure-request':'1',
                   'scheme':'https'})

html= resp.text
#print(html)
htmlpath = "C:\\Users\\priya\\Desktop\\ML\\data_2.html"
page_fun = open(htmlpath,'w',encoding = 'utf-8')
page_fun.write(html)
soup = BeautifulSoup(html,'lxml')

file = open("scraoed_data.txt","w")
info = Data_extract(soup)
for i in info:
    file.write(i)

file.close()
page_fun.close()
