from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from .util import click


class Account(object):
    _username: str

    def __init__(self, username: str, password: str, driver_desktop=None, driver_mobile=None):
        self.username = username
        self.password = password
        self.driver_desktop = driver_desktop
        self.driver_mobile = driver_mobile

    def login_desktop(self):
        driver = self.driver_desktop
        driver.get("https://www.instagram.com/")
        time.sleep(2)

        username_box = driver.find_element_by_xpath(
            "//input[@name='username']")
        username_box.clear()
        username_box.send_keys(self.username)

        password_box = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_box.clear()
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.RETURN)
        time.sleep(3)

        not_now_button = driver.find_element_by_xpath("//a[@href='/']")
        not_now_button.click()

        time.sleep(2)

    def login_mobile(self):
        driver = self.driver_mobile
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        login_button = driver.find_element_by_xpath(
            "//button[@class='sqdOP  L3NKy   y3zKF     ']")
        click(driver, login_button)

        time.sleep(2)
        username_box = driver.find_element_by_xpath(
            "//input[@name='username']")
        username_box.clear()
        username_box.send_keys(self.username)
        password_box = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_box.clear()
        password_box.send_keys(self.password)
        password_box.send_keys(Keys.RETURN)
        time.sleep(3.5)
        not_now = driver.find_element_by_xpath(
            "//button[@class='sqdOP yWX7d    y3zKF     ']")
        click(driver, not_now)
        time.sleep(2)

    def find_username(self):
        driver = self.driver_desktop
        self._username = driver.find_element_by_xpath(
            "//a[@class='gmFkV']").text
