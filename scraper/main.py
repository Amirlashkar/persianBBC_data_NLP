from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/Users/albk/Documents/ChromeDriver/chromedriver_mac_arm64/chromedriver")
driver.get(f"https://www.bbc.com/persian")

items = driver.find_elements(By.XPATH, "//li[@role='listitem' and ./a[contains(text(), '')]]")

topics = ["ايران", "جهان", "افغانستان", "هنر", "ورزش", "اقتصاد", "دانش"]

for item in items:
    if item.text.strip() in topics:
        item.click()
        time.sleep(5)
        driver.back()
        time.sleep(3)