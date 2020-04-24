from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

#quote_plus allows us to encode words that cannot be used in url into usable set of words
base_url = 'https://instagram.com/explore/tags/'
tag_url = input('Type in any tag you would like to search for: ')
url = base_url + quote_plus(tag_url)

#These two lines allow to open the browser in incognito mode
#Not necessary, but just good to know
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path='C:/users/junna/chromedriver.exe', chrome_options=chrome_options)
#Open the url using chrome 
driver.get(url) 
#To prevent the next line of code executing before the page source loads
time.sleep(2)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#Get all the posts
insta = soup.select('.v1Nh3.kIKUG._bz0w')
n = 1
for image in insta:
    image_url = image.select_one('.KL4Bh').img['src']
    with urlopen(image_url) as f:
        #Saving each files name in order
        #Stores pictures in D:\VSPython\img folder
        with open('D:\\VSPython\\img\\' + tag_url + str(n) + '.jpg', 'wb') as h:    
            img = f.read()
            h.write(img)
    n += 1
    print(image_url)
driver.close()