from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C://chromedriver.exe')
driver.get("https://www.reserved.com/ro/ro/customer/account/login/#register")
driver.maximize_window()

sleep(1)

createAccount = driver.find_element(By.XPATH,'//*[@id="email_id"]')
emailInput = driver.find_element(By.XPATH,'//*[@id="email_id"]')
emailInput.send_keys("mihai@reserved.com")

FirstNameInput = driver.find_element(By.XPATH,'//*[@id="firstname_id"]')
FirstNameInput.send_keys("Mihai")

LastNameInput = driver.find_element(By.XPATH,'//*[@id="lastname_id"]')
LastNameInput.send_keys("Popescu")

passwordInput = driver.find_element(By.XPATH,'//*[@id="password_id"]')
passwordInput.send_keys("Abc.1234")
checkBox = driver.find_element(By.CSS_SELECTOR,'#is_subscribed_id')\
checkBox.click()
sleep(2)
createAccountLast = driver.find_element(By.CSS_SELECTOR,'#loginRegisterRoot > div > div.sc-dVNiOx.eRoZWc > div > form > button')
createAccountLast.click()
sleep(1)
duplicateAccount = driver.find_element(By.CSS_SELECTOR,'#loginRegisterRoot > div > div.sc-dVNiOx.eRoZWc > div > div.sc-kYHenr.hqKtAx')

assert duplicateAccount
print("you have already registred with this email adress")


driver.close