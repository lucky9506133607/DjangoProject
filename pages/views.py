from django.views.generic import TemplateView
from django.shortcuts import render
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.by import By
import time

def HomeView(request):
    print('Home page started')
    if request.method == "POST":
        print("Inside Post API")
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
        driver.get("https://hrms.orangetechnolab.com/")
        print("get URL update")
        time.sleep(10)
        gettitle = driver.title
        print("driver title get")
        print(f'************** {gettitle} **************')    
        time.sleep(10)
        print(Valid_user[0])
        print('code Successfully worked')
        return render(request,'home.html', {'key': gettitle})        
    return render(request,'home.html')        
