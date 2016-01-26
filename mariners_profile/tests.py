from django.test import LiveServerTestCase

from selenium import webdriver

import time

class ApplicationFormTestCase(LiveServerTestCase):
	# app name = application_form
	# URL = /application-form/
	def setUp(self):
		self.selenium = webdriver.Firefox()
		self.selenium.maximize_window()
		super(ApplicationFormTestCase, self).setUp()

	def tearDown(self):
		# Call tearDown to close the web browser
		time.sleep(3)
		self.selenium.quit()
		super(ApplicationFormTestCase, self).tearDown()

	def test_login_application_form(self):
		# Logs-in on the application form
		self.selenium.get('%s' % ("http://192.168.0.50:8000/"))

		# Fill the credentials of username and password
		username = self.selenium.find_element_by_id("id_username")
		username.send_keys('tvla')
		password = self.selenium.find_element_by_id("id_password")
		password.send_keys('tvla')

		# Locate the login button and click it
		self.selenium.find_element_by_id('login-form').submit()