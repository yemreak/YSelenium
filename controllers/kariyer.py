# Tek başına çalışmak isterse
if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.getcwd())

from utils.chromedriver import *
from utils.common import *
from utils import config

# # PATH Ayarı
# try:
#     os.environ['PYTHONPATH']
# except:
#     sys.path.append(os.getcwd())
# finally:
#     from utils.chromedriver import *


driver = create()

URL = r"https://www.kariyer.net/is-ilanlari/stajyer#&lpst=8"
SCRIPT_PATH = r"javascripts/kariyer.js"

try:
    driver.get(URL)

    # Bir tane elamanın oluşmasını bekleme
    wait_until(driver, Condition.EXIST, By.ID, "ilan0")

    # Ana scriptleri çalıştırma
    execute_script(driver, SCRIPT_PATH, file=True)

    # Dosyayı oluşturma
    first_info = True
    with open(config.FILE_OUT, "a") as file:
        file.write("[")

    # Her Sayfa için devam edecek
    while True:
        # Linkleri belleğe alma
        execute_script(driver, r"regLinks()")

        # Yeni linke basabildiği sürece devam edecek
        while execute_script(driver, r"return clickLink()"):
            # Link indeksi hesaplama
            if config.LOGGER:
                link_index = driver.execute_script(r"return reg.link_index")

            switch_tab(driver, 1)

            log_to_file()

            # Ana scriptleri çalıştırma
            execute_script(driver, SCRIPT_PATH, file=True)

            # Sayfanın en altına inme (bazı alanlar yüklenmiyor)
            execute_script(
                driver,
                "window.scrollTo(document.body.scrollWidth / 2, document.body.scrollHeight / 3);"
            )

            try:
                # Yükleme alanlarının gelmesini bekleme
                wait_until(
                    driver, Condition.EXIST_ALL,
                    By.CSS_SELECTOR, "div.knetLoadingBig"
                )

                # Ayrılmasını bekleme
                wait_until(
                    driver, Condition.REMOVED,
                    By.CSS_SELECTOR, "div.knetLoadingBig"
                )

                # Verileri dosyaya yazma
                with open(config.FILE_OUT, "a") as file:
                    # İlk eleman değilse , ile ayırma
                    if not first_info:
                        file.write(",")
                    else:
                        first_info = False

                    # Verileri yazma
                    # TODO Null geliyor bir öğe try catch f,kur
                    file.write(
                        to_json(driver.execute_script("return getInfo()"))
                    )

            except se.TimeoutException:
                if config.LOGGER:
                    with open(config.FILE_LOGGER, "a") as file:
                        file.write(
                            f"{config.LOG_WARNING} - {link_index}. link '{driver.title}' için içerik beklemesinde hata meydana geldi.\n")

            # Sekmeyi kapatıp ana sekmeye yönelme
            driver.close()
            switch_tab(driver, 0)

        # İçeriği değişim kontrolü için kayıt altında tutma
        link = execute_script(driver, "return checkIfLinkChanged()")

        # Yeni bir sayfa varsa devam, yoksa döngüden çıkma
        if not execute_script(driver, r"return nextPage()"):
            break

        # İçerik değişene kadar bekleme
        while True:
            time.sleep(1)  # Sistemi çok yormayı engelleme
            if link != execute_script(driver, "return checkIfLinkChanged()"):
                break

finally:
    # Dosyaya son karakteri ekleme
    with open(config.FILE_OUT, "a") as file:
        file.write("]")

    # Driver'ı kapatma
    close_all(driver)
