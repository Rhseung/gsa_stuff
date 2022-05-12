from selenium import webdriver

options = webdriver.ChromeOptions()
Driver = webdriver.Chrome(executable_path="C:/Users/SAMSUNG/Desktop/chromedriver.exe", options=options)
Driver.implicitly_wait(3)
Driver.get('https://www.acmicpc.net/')
Driver.find_element_by_xpath(f'/html/body/div[2]/div[1]/div[1]/div/ul/li[3]/a').click()
Driver.find_element_by_xpath(f'/html/body/div[2]/div[3]/div/div/form/div[2]/input').send_keys('rhseung')
Driver.find_element_by_xpath(f'/html/body/div[2]/div[3]/div/div/form/div[3]/input').send_keys('rhs060224')
Driver.find_element_by_xpath(f'/html/body/div[2]/div[3]/div/div/form/div[4]/div[2]/button').click()