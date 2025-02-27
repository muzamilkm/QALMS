from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from chromedriver.chromedriver import *
def lmsLogin(username, password):
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.headless = True          #set the headless option
    driver = webdriver.Chrome(chromedriverpath, options=chrome_options)

    # head to github login page
    driver.get("https://lms.nust.edu.pk/portal/login/index.php")
    # find username/email field and send the username itself to the input field
    #print(username)
    driver.find_element(By.ID, 'username').send_keys(username)
    # find password input field and insert password as well
    #print(password)
    driver.find_element(By.ID, 'password').send_keys(password)
    # click login button
    driver.find_element(By.ID,"loginbtn").click()

    # wait the ready state to be complete
    WebDriverWait(driver=driver, timeout=10).until(
        lambda x: x.execute_script("return document.readyState === 'complete'")
    )
    error_message = "Incorrect username or password."
    currentURL = driver.current_url
    if currentURL == "https://lms.nust.edu.pk/portal/my/":
        #print("Login successful")
        return "Login Successful"
    else:
        #print("Login failed")
        return "Login failed"
    driver.close()
