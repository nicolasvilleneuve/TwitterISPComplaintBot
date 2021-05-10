from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 500
PROMISED_UP = 500
TWITTER_ACCT = 'YOUR TWITTER ACCT NAME'
TWITTER_PASS = 'YOUR TWITTER ACCT PASSWORD'


chromedriver = "PATH TO YOUR CHROME DRIVER"



class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP
        self.down_speed = 0
        self.up_speed = 0

    def get_internet_speed(self):
        self.driver.get(url='https://www.speedtest.net/')
        to_isp = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        to_isp.click()
        time.sleep(60)
        download_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down_speed = download_speed.text
        upload_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        self.up_speed = upload_speed.text

    def tweet_at_provider(self, down_speed, up_speed):
        self.driver.get(url='https://twitter.com/?login')
        time.sleep(5)
        begin_login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div')
        begin_login.click()
        time.sleep(3)
        username = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_ACCT)
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        text_box = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        text_box.send_keys(f'hey @Bell_Support, how come I am paying for Fibe 500 (500Mbps down and up), yet I am only getting {down_speed}Mbps down and {up_speed}Mbps up???')



bot = InternetSpeedTwitterBot(chromedriver)
bot.get_internet_speed()
time.sleep(5)
bot.tweet_at_provider(bot.down_speed, bot.up_speed)
