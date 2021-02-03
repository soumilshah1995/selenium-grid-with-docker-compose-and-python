try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    print("All Modules are loaded")
except Exception as e:
    print("Error : {} ".format(e))

driver = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME,
)

URL = "https://www.rd.com/jokes/"
driver.get(url=URL)
print(driver.page_source)


