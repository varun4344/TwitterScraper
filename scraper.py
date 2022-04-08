import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

class SeleniumClient:
    def __init__(self):
        self.USERNAME = "XXXXXXXXXXX"
        self.PASSWORD = "XXXXXXXXXXX"

        #Enter Your path for Chrome Driver below

        self.chrome_driver_path = "C:\Development\chromedriver.exe"

        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)


    def twitterLogin(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(3)
        self.userNameField = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')\

        self.userNameField.send_keys(self.USERNAME)

        self.nextbut = self.driver.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
        self.nextbut.click()
        time.sleep(3)
        self.passwordField = self.driver.find_element_by_name('password')
        self.passwordField.send_keys(self.PASSWORD)

        self.passwordField.send_keys(Keys.ENTER)

    def scrapeTweets(self):
        body=self.driver.find_element_by_tag_name('body')
        for i in range(20):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)

        timeline = self.driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
        card = timeline[1]

    def getTweetData(self,card):
        username=card.find_element_by_xpath('.//span').text
        content =card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
        tweet = (username,content)