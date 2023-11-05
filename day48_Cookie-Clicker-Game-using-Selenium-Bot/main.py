import time
from selenium import webdriver
from selenium.webdriver.common.by import By

CURSOR_COOKIES = 15
GRANDMA_COOKIES = 100
FACTORY_COOKIES = 500
MINE_COOKIES = 2000
SHIPMENT_COOKIES = 7000
ALCHEMY_LAB_COOKIES = 50000
PORTAL_COOKIES = 1000000
TIME_MACHINE_COOKIES = 123456789

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


def buy_cookies(cookies_money):
    if cookies_money >= CURSOR_COOKIES and cookies_money < GRANDMA_COOKIES:
        return driver.find_element(By.ID,"buyCursor").click()
    elif cookies_money >= GRANDMA_COOKIES and cookies_money < FACTORY_COOKIES:
        return driver.find_element(By.ID, "buyGrandma").click()
    elif cookies_money >= FACTORY_COOKIES and cookies_money < MINE_COOKIES:
        return driver.find_element(By.ID, "buyFactory").click()
    elif cookies_money >= MINE_COOKIES and cookies_money < SHIPMENT_COOKIES:
        return driver.find_element(By.ID, "buyMine").click()
    elif cookies_money >= SHIPMENT_COOKIES and cookies_money < ALCHEMY_LAB_COOKIES:
        return driver.find_element(By.ID, "buyShipment").click()
    elif cookies_money >= ALCHEMY_LAB_COOKIES and cookies_money < PORTAL_COOKIES:
        return driver.find_element(By.ID, "buyAlchemy lab").click()
    elif cookies_money >= PORTAL_COOKIES and cookies_money < TIME_MACHINE_COOKIES:
        return driver.find_element(By.ID, "buyPortal").click()
    else:
        return driver.find_element(By.ID, "buyTime machine").click()


cookies = driver.find_element(By.ID, "cookie")
current_time = time.time()
timeout = time.time() + 60 * 5
seconds = time.time() + 5
while True:
    cookies.click()
    if time.time() > seconds:
        money = (driver.find_element(By.ID, "money")).text.split(",")
        "".join(money)
        buy_cookies(cookies_money=int(money[0]))
        seconds += 5
    if time.time() > timeout:
        cookies_per_second = driver.find_element(By.ID, "cps")
        print(cookies_per_second.text)
        break

