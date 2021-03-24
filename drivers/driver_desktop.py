from selenium import webdriver

from ..env import GECKO

desktop_driver = webdriver.Firefox(executable_path=GECKO)