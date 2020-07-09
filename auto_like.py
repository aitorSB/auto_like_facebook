import sys
import getpass
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def dataLogin():
    data = []
    email = input("Enter your email: ")

    if not email:
        dataLogin()

    data.append(email)
    password = getpass.getpass("Enter your password: ")
    data.append(password)

    return data

def scroll(driver):
    driver.execute_script("window.scrollBy(0, window.innerHeight + 300)")

def getLikes(driver):
    likes = driver.find_elements_by_xpath('//div[@aria-label=\"Me gusta\"]')
    if not likes:
        likes = driver.find_elements_by_xpath('//div[@aria-label=\"Like\"]')
    return likes

def setLikes(likes, driver):
    try:
        if driver.title == "Facebook" and likes:
            for like in likes:
                like.click()
                scroll(driver)
                sleep(3)
            return 1
        else:
            print("try again")
            return 0  
    except:
        print('can not click in this element')
        return 1

def initFacebook(data):

    profile = webdriver.FirefoxProfile()
    driver = webdriver.Firefox(profile)

    email = data[0]
    password = data[1]

    driver.get('https://www.facebook.com/')

    sleep(5)
    login = driver.find_element_by_name("email")
    login.clear()
    login.send_keys(email)
    login = driver.find_element_by_name("pass")
    login.send_keys(password)  
    login.send_keys(Keys.RETURN)
    sleep(10)
    
    return driver

def main():
    data = dataLogin()
    if data:
        driver = initFacebook(data)
        if driver:
            likes = getLikes(driver)
            if likes:
                setting_likes = setLikes(likes, driver)
                while setting_likes == 1:
                    likes = getLikes(driver)
                    if likes:
                        setting_likes = setLikes(likes, driver)
                main()
    
if __name__ == '__main__':
    main()