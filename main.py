import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# can also use path, but above is best practice so can be PATH = '/Users/sobia/chromedriver-mac-x64/chromedriver'
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# if we do something on Selenium, once done the browser closes.
# To leave browser open even if everything is completed the following 2 lines do the trick:
options = Options()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://www.mwave.me/en/")
# I prefer the full screen opening so the line below will do that:
driver.maximize_window()
# If wanting to ask to give across whole page a tags that have an href attribute:
links = driver.find_elements("xpath", "//a[@href]")
for link in links:
    # Can get attribute by saying innerHTML which is the text of whatever is inside the anchor tag
    # print(link.get_attribute("innerHTML"))
    if "SIGNED CD" in link.get_attribute("innerHTML"):
        link.click()
        break

# cd_links = driver.find_elements("xpath", "//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., 'P1Harmony')]]][count(.//a)=2]//a")
#
# cd_links[0].click()
#
# driver.switch_to.window(driver.window_handles[1])
#
# time.sleep(3)
# buttons = driver.find_elements("xpath", "//a[.//span[text()[contains(., 'P1Harmony')]]]//span[text()[contains(., '$')]]")
#
# for button in buttons:
#     print(button.get_attribute("innerHTML"))
