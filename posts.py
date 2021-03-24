import os
from typing import List

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from .util import click


class Posts(object):

    def __init__(self, driver_mobile):
        self.driver = driver_mobile

    def send_post(self, img: str, text: str, tags: List[str]):
        driver = self.driver

        driver.get("https://www.instagram.com/")
        time.sleep(2)

        new_post = driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav[2]/div/div/form/input")
        self.click(driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]"))
        new_post.send_keys(os.getcwd()+img)
        time.sleep(2)

        avancar = driver.find_element_by_xpath("//button[@class='UP43G']")
        self.click(avancar)

        time.sleep(2)

        text_area = driver.find_element_by_xpath("//textarea[@class='_472V_']")
        text_area.clear()
        tags_string = ''.join(e+"\n" for e in tags)
        text_area.send_keys(text+"\n"+tags_string)
        time.sleep(2)

        compartilhar = driver.find_element_by_xpath("//button[@class='UP43G']")
        click(compartilhar)
