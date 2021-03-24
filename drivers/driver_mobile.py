from selenium import webdriver

from ..env import GECKO


def set_driver_mobile():
    user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", user_agent)
    driver_mobile = webdriver.Firefox(
        executable_path=GECKO, firefox_profile=profile)
    driver_mobile.set_window_size(454, 560)
    return driver_mobile


driver_mobile = set_driver_mobile()
