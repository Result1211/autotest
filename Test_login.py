# -*- coding: utf-8 -*-
from model.user import User
from selenium import webdriver
from selenium.common.exceptions import *
from selenium_fixture import app


def logout(driver):
    driver.find_element_by_link_text("Выйти").click()

def login(driver, user):
    driver.find_element_by_id("user_email").click()
    driver.find_element_by_id("user_email").clear()
    driver.find_element_by_id("user_email").send_keys(user.user_email)
    driver.find_element_by_id("user_password").click()
    driver.find_element_by_id("user_password").clear()
    driver.find_element_by_id("user_password").send_keys(user.user_password)
    driver.find_element_by_name("commit").click()


def test_auto(app):
    app.driver.get("http://kuki.webtest2.htc-cs.com/" + "/users/login")
    login(app.driver, User.Admin())
    logout(app.driver)
