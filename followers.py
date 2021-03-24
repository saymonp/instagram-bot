from typing import List
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from .util import click

class Followers(object):
    following_accounts: List[str]
    follower_accounts: List[str]

    def __init__(self, driver_desktop):
        self.driver = driver_desktop

    def find_followings(self, buttons):
        driver = self.driver

        self.following_button = [button for button in buttons if 'following' in button.get_attribute('href')]
        self.following_button[0].click()
        time.sleep(2)

        followingsList = lambda: driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowingsInList = len(followingsList().find_elements_by_css_selector('li'))
        following_number = lambda: driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text
        followingsList().click()

        actionChain = webdriver.ActionChains(driver)
        count = 0
        while (numberOfFollowingsInList < int(following_number())):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            print(numberOfFollowingsInList, int(following_number()))
            numberOfFollowingsInList = len(followingsList().find_elements_by_css_selector('li'))
            count += 1
            print(count)
            if count > int(following_number()) / 5:
                if int(following_number()) - numberOfFollowingsInList < 3:
                    break

        self.following_accounts = []
        for user in followingsList().find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')

            self.following_accounts.append(userLink)
            if (len(self.following_accounts) == int(following_number())):
                break

        print("seguindo", self.following_accounts)
        element = driver.find_element_by_xpath("//button[@class='wpO6b  ']")
        ActionChains(driver).move_to_element(element).click().perform()

    def find_followers(self, buttons):  
        driver = self.driver

        follower_button = [button for button in buttons if 'followers' in button.get_attribute('href')]
        follower_button[0].click()
        time.sleep(2)

        followersList = lambda: driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList().find_elements_by_css_selector('li'))
        follower_number = lambda: driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text

        followersList().click()
        actionChain = webdriver.ActionChains(driver)
        count = 0
        while (numberOfFollowersInList < int(follower_number())):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList().find_elements_by_css_selector('li'))
            print(numberOfFollowersInList, int(follower_number()))
            count += 1
            print(count)
            if count > int(follower_number()) / 5:
                if int(follower_number()) - numberOfFollowersInList < 3:
                    break

        time.sleep(2)
        self.follower_accounts = []
        users = lambda: followersList().find_elements_by_css_selector('li')

        for user in users():
            userLink = lambda: user.find_element_by_css_selector('a')
            userLink = userLink().get_attribute('href')
            self.follower_accounts.append(userLink)
            if (len(self.follower_accounts) == int(follower_number())):
                break

        print("seguidores", self.follower_accounts)
        element = driver.find_element_by_xpath("//button[@class='wpO6b  ']")
        ActionChains(driver).move_to_element(element).click().perform()

    def compare_following_and_followers(self, followers, followings):
        followers = set(self.follower_accounts)
        followings = set(self.following_accounts)
        targetusers = followings - followers
        for acc in targetusers:
            self._blacklist.append(acc)


    def find_target_users(self):
        driver = self.driver
        driver.get("https://www.instagram.com/" + self._username + "/")
        time.sleep(2)

        buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")

        self.find_followings(driver, buttons)
        time.sleep(2)

        buttons = driver.find_elements_by_xpath("//a[@class='-nal3 ']")

        self.find_followers(driver, buttons)
        
        time.sleep(2)
        self.compare_following_and_followers(self.follower_accounts, self.following_accounts)


    def unfollow_by_userlink(self, userlink):
        driver = self.driver
        driver.get(userlink)
        time.sleep(2)

        follow_button = self.driver.find_element_by_xpath("//button[@class='_5f5mN    -fzfL     _6VtSN     yZn4P   ']")
        ActionChains(self.driver).move_to_element(follow_button).click().perform()
        time.sleep(2)
        
        button = self.driver.find_element_by_xpath("//button[@class='aOOlW -Cab_   ']")
        click(driver, button)

    def unfollow_target_users(self, unfollows: int, interval: float):
        """
        Unfollows a given number of users in a given interval time, maximum recommended is 50 per hour.
        Args:
            unfollows:
                The Number of unfollows, maximum recommended is 50 per hour
            interval: 
                Time to wait between the given number of unfollows     
        """
        count = 0

        for userlink in self._blacklist:
            try:
                self.unfollow_by_userlink(userlink)

                count += 1
                print(count)

                if count == unfollows:
                    count = 0
                    time.sleep(interval)
            except:
                continue
        print("Unfollow unfollowers done!")
    
    
        

