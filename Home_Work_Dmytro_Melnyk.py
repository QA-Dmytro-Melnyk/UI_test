import pytest
from time import sleep
import json
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager


URL = "https://the-internet.herokuapp.com/"

class TestTheInternetWebsite():

    def setup_method(self, method):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.vars = {}

    git
    remote
    add
    origin
    git @ github.com: QA - Dmytro - Melnyk / UI_test_automation.git
    def teardown_method(self, method):
        self.driver.quit()

    def test_open_url(self):
        self.driver.get(URL)
        sleep(2)
        assert self.driver.title =='The Internet'



    def test_key_presses(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/key_presses']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Key Presses'
        input_element = self.driver.find_element(By.XPATH, '//input')
        assert input_element.get_attribute('value') == ''
        input_element.send_keys('d')
        assert input_element.get_attribute('value') == 'd'
        self.driver.refresh()
        input_element = self.driver.find_element(By.XPATH, '//input')
        assert input_element.get_attribute('value') == ''
        input_element.send_keys('2')
        assert input_element.get_attribute('value') == '2'


    def test_redirect_link(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/redirector']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Redirection'
        click_here = self.driver.find_element(By.XPATH, "//*[@id='redirect']")
        assert click_here.text == 'here'
        click_here.click()
        assert self.driver.find_element(By.XPATH, '//*[@id="content"]/div/h3').text == 'Status Codes'

    def test_status_codes(self):
        self.driver.get(URL)
        self.driver.find_element(By.XPATH, "//a[@href='/status_codes']").click()
        assert self.driver.find_element(By.XPATH, "//div[@class='example']/h3").text == 'Status Codes'

        click_on_here = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/p[1]/a')
        assert click_on_here.text == 'here'
        click_on_here.click()
        assert self.driver.find_element(By.XPATH, '/html/body/article/h1').text == 'Hypertext Transfer Protocol (HTTP) Status Code Registry'
        self.driver.back()

        click_on_200 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/a')
        click_on_200.click()
        assert self.driver.find_element(By.XPATH, '//*[@id="content"]/div/h3').text == 'Status Codes'

        back_to_page_status_code = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/p/a')
        back_to_page_status_code.click()
        assert self.driver.find_element(By.XPATH, '//*[@id="content"]/div/h3').text == 'Status Codes'


        click_on_301 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/a')
        click_on_301.click()
        assert self.driver.find_element(By.XPATH, '//*[@id="content"]/div/h3').text == 'Status Codes'


        back_to_page_status_code = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/p/a')
        back_to_page_status_code.click()
        assert self.driver.find_element(By.XPATH, '//*[@id="content"]/div/h3').text == 'Status Codes'

        click_on_404 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/a')
        click_on_404.click()
        assert self.driver.find_element(By.XPATH, '//*[@id="content"]/div/h3').text == 'Status Codes'

        back_to_page_status_code = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/p/a')
        back_to_page_status_code.click()
        assert self.driver.find_element(By.XPATH, '//*[@id="content"]/div/h3').text == 'Status Codes'

        click_on_500 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[4]/a')
        click_on_500.click()
        assert self.driver.find_element(By.XPATH, '//*[@id="content"]/div/h3').text == 'Status Codes'

        back_to_page_status_code = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/p/a')
        back_to_page_status_code.click()
        assert self.driver.find_element(By.XPATH, '//*[@id="content"]/div/h3').text == 'Status Codes'