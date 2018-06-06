# -*- coding: utf-8 -*-
class Application(object):

    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get("http://kuki.webtest2.htc-cs.com/"+"users/login")

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Выйти").click()

    def login(self, user):
        driver = self.driver
        driver.find_element_by_id("user_email").click()
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys(user.user_email)
        driver.find_element_by_id("user_password").click()
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys(user.user_password)
        driver.find_element_by_name("commit").click()