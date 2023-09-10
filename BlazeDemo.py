import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))


driver.get("https://www.demoblaze.com/index.html")


SignUp = driver.find_element(By.ID, "signin2")
SignUp.click()
driver.implicitly_wait(5)

SignUpUsername = driver.find_element(By.ID, "sign-username")
SignUpUsername.click()
SignUpUsername.send_keys("yehey")
driver.implicitly_wait(5)

SignUpPassword = driver.find_element(By.ID, "sign-password")
SignUpPassword.click()
SignUpPassword.send_keys("yehey")
driver.implicitly_wait(5)

BtnSignup = driver.find_element(By.XPATH, "//button[contains(text(),'Sign up')]")
BtnSignup.click()
time.sleep(5)
driver.switch_to.alert.accept()


LogIn = driver.find_element(By.ID, "login2")
LogIn.click()
driver.implicitly_wait(5)


LogInUsername = driver.find_element(By.CSS_SELECTOR, "#loginusername")
LogInUsername.click()
LogInUsername.send_keys("yehey")

LoginPassword = driver.find_element(By.CSS_SELECTOR, "#loginpassword")
LoginPassword.click()
LoginPassword.send_keys("yehey")
driver.implicitly_wait(15)


Button = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]")
Button.click()
time.sleep(5)

LogOut = driver.find_element(By.XPATH, "//a[@id='logout2']")
LogOut.click()
driver.implicitly_wait(10)

driver.execute_script("alert('Requirements Completed!');")
