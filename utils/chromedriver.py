"""Chromedriver İşlemleri
"""

if __name__ == "__main__":
    print("Yardımcı modüldür, doğrudan çalıştırılamaz")
    exit()
else:
    from utils import config
    from enum import Enum, unique

    from jsmin import jsmin
    from selenium import webdriver
    from selenium.common import exceptions as se
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait


@unique
class Condition(Enum):
    EXIST = EC.presence_of_element_located
    EXIST_ALL = EC.presence_of_all_elements_located
    REMOVED = EC.invisibility_of_element_located


def create(hidden: bool = config.HIDE_BROWSER) -> webdriver:
    """Chromedriver'ı hazırlama

    Keyword Arguments:
    hidden {bool} -- GUI modunu devre dışı bırakma (default: {HIDE_BROWSER})
    """

    options = webdriver.ChromeOptions()

    if hidden:
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-setuid-sandbox')

    # Driver öğesini oluşturma
    return webdriver.Chrome(
        executable_path=config.CHROMEDRIVER_PATH,
        options=options
    )


def execute_script(driver: webdriver, script: str, file=False):
    """Javascript Derleme

    Arguments:
        script {str} -- Javscript ya da dosya yolu

    Keyword Arguments:
        file {bool} -- Dosya yolu verirse true olmalı (default: {False})
    """

    def minify(file_path):
        with open(file_path) as js_file:
            return jsmin(js_file.read(), quote_chars="'\"`")

    return driver.execute_script(minify(script) if file else script)


def wait_until(driver: webdriver, condition, by: str, value: str, time=config.DEFAULT_TIMEOUT) -> None:
    WebDriverWait(driver, time).until(condition.value(((by, value))))


def close_all(driver):
    tabs = driver.window_handles  # Sekme bilgilerini alma
    for tab in tabs:
        driver.switch_to.window(tab)  # Açılan sekmeye geçme
        driver.close()


def switch_tab(driver: webdriver, tab_index: int):
    tabs = driver.window_handles  # Sekme bilgilerini alma
    driver.switch_to.window(tabs[tab_index])  # Açılan sekmeye geçme
