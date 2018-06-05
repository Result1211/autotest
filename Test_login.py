# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium_fixture import driver
import unittest, time, re


def logout(driver):
    driver.find_element_by_link_text("Выйти").click()

def login(driver):
    driver.find_element_by_id("user_email").click()
    driver.find_element_by_id("user_email").clear()
    driver.find_element_by_id("user_email").send_keys("test10@test.ru")
    driver.find_element_by_id("user_password").click()
    driver.find_element_by_id("user_password").clear()
    driver.find_element_by_id("user_password").send_keys("tester10")
    driver.find_element_by_name("commit").click()

def test_auto(driver):
    driver.get("http://kuki.webtest2.htc-cs.com/" + "/users/login")
    login(driver)
    logout(driver)
