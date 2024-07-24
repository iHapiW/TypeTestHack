#!/usr/bin/env python3

from time import sleep
from random import uniform

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument(f'--load-extension=/home/ihapiw/.config/google-chrome/Default/Extensions/gcknhkkoolaabfmlnjonogaaifnjlfnp/8.9_0')
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)
driver.get("https://typetest.io")

while True:
    input()
    while True:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "test-char"))
        )

        test_text = driver.find_elements(By.CLASS_NAME, "test-char")
        correct = driver.find_elements(By.CLASS_NAME, "correct")
        incorrect = driver.find_elements(By.CLASS_NAME, "incorrect")

        brk = False

        txt = ""
        for i in test_text:
            try:
                attrs = i.get_attribute("class").split(' ')
                if "correct" not in attrs and "incorrect" not in attrs:
                    txt += i.text
            except:
                brk = True
                break

        if brk:
            break

        inp = driver.find_element(By.ID, "test-input")

        i = 0
        while i != len(txt)-1:
            try:
                inp.send_keys(txt[i])
                sleep(uniform(0.01, 0.04))
                i += 1
            except:
                brk = True
                break
        if brk:
            break
