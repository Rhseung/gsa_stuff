from selenium import webdriver

options = webdriver.ChromeOptions()
Driver = webdriver.Chrome(executable_path="C:/Users/SAMSUNG/Desktop/chromedriver.exe", options=options)
Driver.implicitly_wait(3)
Driver.get('http://lms.gsa.hs.kr/login/index.php')
Driver.find_element_by_xpath(f'/html/body/div[3]/div/section/div/div/div/div/form/div[1]/div[2]/input').send_keys('22027')
Driver.find_element_by_xpath(f'/html/body/div[3]/div/section/div/div/div/div/form/div[1]/div[5]/input').send_keys('qaescxz224')
Driver.find_element_by_xpath(f'/html/body/div[3]/div/section/div/div/div/div/form/input[2]').click()