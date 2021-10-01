from selenium import webdriver
import time

CHROMEDRIVER = "C://Users/Carlo/desktop/Development/chromedriver.exe"
driver = webdriver.Chrome(CHROMEDRIVER)
driver.maximize_window()
driver.get("https://www.instagram.com/")

username = ENTER USER NAME HERE
password = ENTER PASSWORD HERE


time.sleep(2)
name_input = driver.find_element_by_name("username")
name_input.send_keys(username)
time.sleep(2)
password_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password_input.send_keys(password)
time.sleep(2)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
login.click()

time.sleep(2)
search_query = driver.find_element_by_class_name("XTCLo")
search_query.send_keys("Naruto")
time.sleep(2)
select = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[2]/a')
select.click()

time.sleep(2)
check_followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
check_followers.click()

time.sleep(2)
follow = driver.find_elements_by_css_selector('button.sqdOP')

for i in follow:
    if i.text == "Follow":
        time.sleep(2)
        i.click()
        print("Follow made")
    else:
        print("skipped over")
        pass

exit_div = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/button')
exit_div.click()

time.sleep(2)
go_to_profile = driver.find_element_by_css_selector('span._2dbep.qNELH')
go_to_profile.click()

time.sleep(2)
render_profile = driver.find_element_by_css_selector('div._01UL2>a')
render_profile.click()
