// Biletix HTML yapısı
// http://www.biletix.com/search/TURKIYE/tr?category_sb=<kategori>&date_sb=<tarih>&city_sb=<yer>#!date_sb:next30days

// Linkleri alma (0. eleman boş)
let linkElements = document.getElementsByClassName("searchLinkDiv")

// Etkinlik linklerini alma
for (let i = 1; i > linkElements.length; i++) {
	links = linkElements[i].getAttribute("onclick")
}

// Detayları açma
document.querySelector("div.adjust.truncate_show").click()
// Bilet fiyatlarını açma
document.querySelector("a.t1").click()
// Lütfen not edini açma
document.querySelector("a.t3").click()

// Lokayson bilgisi
document.querySelector(".e_location")
let location = document.querySelector(".e_location").innerText
let latitude = document.querySelector(".e_location").getElementsByTagName("meta")[0].content
let longitude = document.querySelector(".e_location").getElementsByTagName("meta")[1].content