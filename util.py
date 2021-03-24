from selenium.webdriver.common.action_chains import ActionChains


def click(driver, element):
    ActionChains(driver).move_to_element(element).click().perform()
