#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from config import GECKO_PATH, FIREFOX_PATH, GECKO_LOG_PATH

class Browser:
	def __init__(self):
		# Setting up the Browser
		self.options = Options()
		self.options.binary_location = FIREFOX_PATH
		#self.options.headless = True
		self.driver = webdriver.Firefox( executable_path=GECKO_PATH    \
                                       , options=self.options          \
                                       , service_log_path=GECKO_LOG_PATH)

	def loadWeb(self, url):
		# Get the web from the internet
		self.driver.get(url)
		html = self.driver.page_source
		#self.driver.close()
		# Return the HTML code
		return html

	def quit(self):
		self.driver.quit()
