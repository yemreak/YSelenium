# Selenium

![GitHub last commit](https://img.shields.io/github/last-commit/yedhrab/YSelenium.svg?label=Son%20G%C3%BCncelleme&style=popout)
![GitHub](https://img.shields.io/github/license/yedhrab/YSelenium.svg?label=Lisans&style=popout)
![GitHub repo size](https://img.shields.io/github/repo-size/yedhrab/YSelenium.svg?label=Boyut&style=popout)

## Selenium Notları

<!-- TODO Selenium notlarını arttık, YSelenium dökümanına ekle -->

- Colab üzerinde (GUI'siz platformlarda) kullanılmak istenirse GUI kapatılmalıdır.
  - `config.py` içerisindeki `HIDE_BROWSER` `True` olmalı
- Javascript'ler *minify* edilmek zorunda aksi halde çalışmaz.
- Javascript'ler her sekme için ayrıca dahil edilmelidir.
- Global fonksiyonlar `window.` formatında olmalıdır
  - Python içerisinde kullanımda `window` yazmaya gerek yoktur
  - Örn: `window.temp = 5`, pythonda kullanım `driver.execute_script('return temp')`
- `driver` objesi 1 sekmeyi temsil etmekte
  - `driver.close` denirse o sekme kapanır
  - `driver.switch_to.window(driver.window_handles[1])` ile sekme arası yolculuk

## TODO

- [ ] Config için açıklama dökümanı ekle

## Lisans ve Teferruatlar

Bu yazı **MIT** lisanslıdır. Lisanslar hakkında bilgi almak için [buraya](https://choosealicense.com/licenses/) bakmanda fayda var.

- [Github](https://github.com/yedhrab)
- [Website](https://yemreak.com)
- [LinkedIn](https://www.linkedin.com/in/yemreak/)

> Yardım veya destek için [iletişime](mailto::yedhrab@gmail.com?subject=YSelenium%20%7C%20Github) geçebilrsiniz 🤗

~ Yunus Emre Ak
