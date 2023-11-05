from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the browser opened after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://python.org")

event_time = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li time")
event = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
n = 0
event_dict = {}

while n < len(event_time):
    event_dict[n] = {
            'time': event_time[n].text,
            'name': event[n].text
        }
    n += 1

print(event_dict)

# driver.close()
driver.quit()
