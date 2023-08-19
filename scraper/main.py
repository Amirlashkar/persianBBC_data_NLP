from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/Users/albk/Documents/ChromeDriver/chromedriver_mac_arm64/chromedriver")
driver.get(f"https://www.bbc.com/persian")
driver.maximize_window()


def check_exists(by:str, target:str):
    try:
        if by == "XPATH":
            driver.find_element(By.XPATH, target)
        elif by == "ID":
            driver.find_element(By.ID, target)
        elif by == "CLASS_NAME":
            driver.find_element(By.CLASS_NAME, target)
        elif by == "LINK_TEXT":
            driver.find_element(By.LINK_TEXT, target)
        elif by == "TAG_NAME":
            driver.find_element(By.TAG_NAME, target)
    except NoSuchElementException:
        return False
    except StaleElementReferenceException:
        return False
    return True

def wait_till_located(by:str, target:str, timestamp:int=1):
    while check_exists(by, target) == False:
        print("Loading page...")
        time.sleep(timestamp)


items = driver.find_elements(By.XPATH, "//li[@role='listitem' and ./a[contains(text(), '')]]")
topics = ["ايران", "جهان", "افغانستان", "هنر", "ورزش", "اقتصاد", "دانش"]

for item in items:
    if item.text.strip() in topics:
        item.click()
        wait_till_located("XPATH", "//ul[@role='list']")
        news_list = driver.find_elements(By.XPATH, "//ul[@role='list' and @data-testid='topic-promos']/li")
        for news in news_list:
            act = ActionChains(driver)
            act.move_to_element(news)
            act.click(news)
            time.sleep(3)
            driver.back()
        driver.back()
        