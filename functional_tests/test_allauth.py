# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestEmailLogin(StaticLiveServerTestCase):

    fixtures = ['allauth_fixture']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.wait = WebDriverWait(self.browser, 10)

    def tearDown(self):
        self.browser.quit()

    def get_element_by_id(self, element_id):
        return self.browser.wait.until(EC.presence_of_element_located(
                (By.ID, element_id)))

    def get_button_by_id(self, element_id):
        return self.browser.wait.until(EC.element_to_be_clickable(
                (By.ID, element_id)))

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_email_register(self):
        # user goes to the home page
        self.browser.get(self.get_full_url("home"))
        # user can see login button
        email_login = self.get_element_by_id("email_login")
        # user can see register button
        email_register = self.get_element_by_id("email_register")
        # user cannot see logout button
        with self.assertRaises(TimeoutException):
            self.get_element_by_id("logout")
        # make sure the register button links to the correct place
        self.assertEqual(
            email_register.get_attribute("href"),
            self.live_server_url + "/accounts/signup"
        )
        email_register.click()
        # user registers here
        self.get_element_by_id("id_email").send_keys("edith@rhodes.edu")
        self.get_element_by_id("id_password1").send_keys("mynameisedith")
        self.get_element_by_id("id_password2").send_keys("mynameisedith")
        sign_up_button = self.browser.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//form[@id='signup_form']/button[1]")
        ))
        sign_up_button.click()
        # user can see the logout button
        logout = self.get_element_by_id("logout")
        # user cannot see the register button
        with self.assertRaises(TimeoutException):
            self.get_element_by_id("email_register")
        # user cannot see the login button
        with self.assertRaises(TimeoutException):
            self.get_element_by_id("email_login")
        logout.click()
        # user can once again see the login button
        email_login = self.get_element_by_id("email_login")
        # user can once again see the register button
        email_register = self.get_element_by_id("email_register")

    def test_email_login(self):
        # user goes to the home page
        self.browser.get(self.get_full_url("home"))
        # user can see login button
        email_login = self.get_element_by_id("email_login")
        # user can see register button
        email_register = self.get_element_by_id("email_register")
        # user cannot see logout button
        with self.assertRaises(TimeoutException):
            self.get_element_by_id("logout")
        # make sure the login button links to the correct place
        self.assertEqual(
            email_login.get_attribute("href"),
            self.live_server_url + "/accounts/login"
        )
        email_login.click()
        # user logs in here
        self.get_element_by_id("id_login").send_keys("s@g.com")
        self.get_element_by_id("id_password").send_keys("helloworld")
        login_button = self.browser.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//form[@class='login']/button[1]")
        ))
        login_button.click()

        # user can see the logout button
        logout = self.get_element_by_id("logout")
        # user cannot see the register button
        with self.assertRaises(TimeoutException):
            self.get_element_by_id("email_register")
        # user cannot see the login button
        with self.assertRaises(TimeoutException):
            self.get_element_by_id("email_login")
        logout.click()
        # user can once again see the login button
        email_login = self.get_element_by_id("email_login")
        # user can once again see the register button
        email_register = self.get_element_by_id("email_register")
