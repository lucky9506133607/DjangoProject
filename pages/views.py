from django.views.generic import TemplateView
from django.shortcuts import render
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.by import By
import time


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):  # new
    template_name = "about.html"
    print('Code starting')
    Valid_user = ['et/amd/189@elsner.com']
    Valid_pass = ['Lucky@123']
    chrome_options = Options()
    print("chrome_options")
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    print("binary_location")
    chrome_options.add_argument("--headless")
    print("headless")
    chrome_options.add_argument("--no-sandbox")
    print("sandbox")
    chrome_options.add_argument("--disable-dev-sh-usage")
    print("disable-dev-sh-usage")
    driver = webdriver.Chrome(service=Service(executable_path=os.environ.get("CHROMEDRIVER_PATH")), chrome_options=chrome_options)
    print("executable_path")
    time.sleep(10)
    driver.get("https://www.google.com/")
    print("get URL")
    time.sleep(10)
    gettitle = driver.title
    print("driver title get")
