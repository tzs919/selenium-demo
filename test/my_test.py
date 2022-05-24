
from selenium.webdriver import Chrome
import selenium.webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with Chrome() as driver:
    # wait = WebDriverWait(driver, 10)
    # webdriver.DesiredCapabilities
    #
    # PROXY = "127.0.0.1:2802"
    # webdriver.DesiredCapabilities['proxy'] = {
    #     "httpProxy": PROXY,
    #     "ftpProxy": PROXY,
    #     "sslProxy": PROXY,
    #     "proxyType": "MANUAL",
    # }


    driver.get("https://www.google.com/")
    driver.implicitly_wait(5)

    # print(EC.title_is("Spitter"))

    print(driver.current_url)
    print(driver.title)
    # print(driver.current_window_handle)
    # print(driver.window_handles)
    # driver.save_screenshot('./image.png')

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.page_load_strategy = 'normal'
# driver = webdriver.Chrome(options=options)
# # Navigate to url
# driver.get("http://www.google.com")
# driver.quit()