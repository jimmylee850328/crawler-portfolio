import imgkit
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 初始化 headless 的 Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# 訪問氣象局網頁
driver.get("https://www.cwa.gov.tw/V8/C/W/Town/Town.html?TID=6300200")
time.sleep(2)

# 使用 Selenium 找到要下載的 element
container_element = driver.find_element(by=By.CSS_SELECTOR, value=".highcharts-container")
svg_content = container_element.get_attribute("outerHTML")

# 關閉瀏覽器
driver.quit()

# 找到 soup 底下所有的 <img> 標籤
soup = BeautifulSoup(svg_content, 'html.parser')
img_tags = soup.find_all('img')
for img_tag in img_tags:
    # image src 加上 domoin
    img_tag['src'] = "https://www.cwa.gov.tw" + img_tag['src']

# 下載成 output.png
imgkit.from_string(soup.prettify(), "./output.png")