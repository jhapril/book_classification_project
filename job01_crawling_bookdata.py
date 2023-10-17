from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re
import time



options = ChromeOptions()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
options.add_argument('user-agent=' + user_agent)
options.add_argument("lang=ko_KR")

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)  # <- options로 변경

category = ['Economy', 'Novel', 'Poetry', 'Humanities', 'Self_development','History', 'Cartoon', 'Magazine']
category_pages = [170, 50917, 50940, 656, 336, 74, 2551, 2913]

url1 = 'https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount=25&ViewType=Detail&PublishMonth=0&SortOrder=2&page='
url2 = '&Stockstatus=1&PublishDay=84&CID=170&SearchOption='

df_titles = pd.DataFrame()
for i in range(8):
    titles = []
    for j in range(1000):
        url = url1 + str(j) + url2
        print(url)


