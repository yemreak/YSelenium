# Tek başına çalışmak isterse
if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.getcwd())

from utils.chromedriver import *
from utils.common import *
from utils import config

# Site yapılandırmaları
PAGE = 100
PAGE_URL = "https://www.gettyimages.com/photos/traffic-light?alloweduse=availableforalluses&family=creative&license=rf&page={}&phrase=traffic%20light&sort=best "
SCRIPT_PATH = "javascripts/gettyImages.js"

# Yükleme Ayarları
DOWNLOAD = False
DOWNLOAD_DIR = "downloads"

# URL Dosyası ayarları
WRITE_FILE = True

# Ek Ayarlar
DEBUG = True


driver = create()
urls = []

try:
    for i in range(PAGE):
        URL = PAGE_URL.format(i + 1)
        driver.get(URL)

        # İstenen öğe yüklenene kadar bekleme
        wait_until(driver, Condition.EXIST, By.CLASS_NAME, "search-content__gallery-assets")

        # Script'i minimize etme ve derleme (Edilmezse çalışmaz)
        page_urls = execute_script(driver, SCRIPT_PATH, file=True)
        urls += page_urls

        if DOWNLOAD:
            download_urls(urls)

        if DEBUG:
            print("Sayfada bulunan url sayısı: ", page_urls.__len__())
            print("Toplam Url Sayısı: ", urls.__len__())

finally:
    if WRITE_FILE:
        # Output dosyasına her url'i yazdırma
        write_array_to_file(OUTPUT_FILE, urls)

    # driver.close()


