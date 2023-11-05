from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://secure-retreat-92358.herokuapp.com/")

fill_form = driver.find_element(By.NAME, "fName")
fill_form.send_keys(
    "Emmanuel",
    Keys.TAB, "Adesoye",
    Keys.TAB,
    "desoyedami@gmail.com",
    Keys.TAB
)
sign_up = driver.find_element(By.CLASS_NAME, "btn")
sign_up.click()
