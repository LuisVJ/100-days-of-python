from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "/home/luis/100-Days-of-Python/projects/day48-Selenium-web-browser/driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

events = driver.find_elements_by_css_selector(".event-widget li")

events_dict = {}
for i in range(len(events)):
    time = events[i].find_element_by_tag_name("time").get_attribute("datetime").split("T")[0]
    events_dict[i] = {
        'time': events[i].find_element_by_tag_name("time").get_attribute("datetime").split("T")[0],
        'name': events[i].find_element_by_tag_name("a").text
    }

print(events_dict)





#driver.close
driver.quit()