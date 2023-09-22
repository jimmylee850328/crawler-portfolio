import html
import re
import time

import cairosvg
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

# 使用 Selenium 找到包含 SVG 元素的 HTML 元素
svg_element = driver.find_element(by=By.CSS_SELECTOR, value=".highcharts-container > svg")

# 等動畫跑完
time.sleep(2)

# 獲取 SVG 元素的 outerHTML
svg_content = svg_element.get_attribute("outerHTML")

# 使用 BeautifulSoup 進行文字分析
soup = BeautifulSoup(svg_content, 'html.parser')
svg_tag = soup.find('svg')

# 替換掉 font-family， svg 才可以正常顯示中文
svg_tag['style'] = re.sub(r"font-family:.*?;", "font-family: Heiti SC Medium;", html.unescape(svg_tag['style']))

# 關閉瀏覽器
driver.quit()

# 使用 cairosvg 將 SVG 轉換為 PNG
cairosvg.svg2png(bytestring=str(svg_tag), write_to='svg-output.png')