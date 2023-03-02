import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager


if os.path.exists("./files") is False:
    os.mkdir("./files")

caminho = str(os.path.dirname(os.path.abspath(__file__))) + "\\files\\"

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option("detach", True)
prefs = {
    "profile.default_content_settings.popups": 0,
    "download.default_directory": caminho,  # IMPORTANT - ENDING SLASH V IMPORTANT
    "directory_upgrade": True,
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://data.anbima.com.br/certificado-de-recebiveis"

driver.get(url)
print("Acessando website")
driver.find_element(By.CLASS_NAME, "pop-up--close-btn").click()
driver.find_element(By.CLASS_NAME, "anbima-ui-toolbar__link").click()
print("Download realizado com sucesso")
