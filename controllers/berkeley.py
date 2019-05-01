from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Yapılandırma areyarları
PATH_CHROME_DRIVER = "utils/chromedriver"
URL = "https://bdd-data.berkeley.edu/login.html"

# Chrome ayarlarını oluşturma (Colab için)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--safebrowsing-disable-download-protection')
# chrome_options.add_argument('--safebrowsing-manual-download-blacklist')

# preferences = {"download.default_directory": "/content", "safebrowsing.enabled": "false"}
# chrome_options.add_experimental_option("prefs", preferences)

# Ayarları belirlenen chrome-driver'ın oluşturulması
driver = webdriver.Chrome(PATH_CHROME_DRIVER)  # , options=chrome_options

# URL'in oluşturulması ve ona bağlanma
driver.get(URL)

# Başlığı tanımlama
title = driver.title

try:
    # Sitede js derleme
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email")))
    script_mail = 'document.getElementById("email").value = "yoif4@alexbox.online"'
    script_pass = 'document.getElementById("password").value = "Temp1234"'
    script_login = 'document.getElementById("login-button").click()'

    driver.execute_script(script_mail)
    driver.execute_script(script_pass)
    driver.execute_script(script_login)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "download")))
    print(driver.current_url)
    script_download = 'downloadChallengeFile(event, "bdd100k/bdd100k_images.zip")'
    driver.execute_script(script_download)
    # Bekleme süresi ekle! (dosya indirilirken)
finally:
    # driver.close()
    pass
