// Kariyer içerik alıcısı

// Veri depolama
window.reg = {}

window.old = () => {
    // Linkler 
    var links = document.querySelectorAll("a.link.position")


    // Genel bilgileri alma
    var content = document.querySelector(".genel-bilgiler").innerText
    var requirements = document.querySelector(".aday-kriterleri").innerText
    var position_details = document.querySelector(".pozisyon-bilgileri").innerText
    var statistics = document.querySelector(".istatistikler").innerText
    var factory_details = document.querySelector(".firma-detay").innerText

    console.log(content, requirements, position_details, statistics, '\n', factory_details)

}

// TODO öğeleri düzenle, güzelleştir, null sorununu çözmek için try catch kur
// TODO Encoded veriyi parçala ve güzelleştir (urlencode)
window.getInfo = () => {
    // İlan başlığından verileri parçalama
    let ad_detail = document.querySelector("div.ilan-detay-top").innerText.split("\n")
    ad_detail = [ad_detail[0], ad_detail[1]].join("\n")

    // Firma detayları varsa alma yoksa 'null' yazma
    let factory_details = document.querySelector(".firma-detay")
    if (factory_details != null) {
        factory_details = factory_details.innerText
    }

    return info = {
        title: ad_detail[0],
        factory: ad_detail[1],
        content: document.querySelector(".genel-bilgiler").innerText,
        requirements: document.querySelector(".aday-kriterleri").innerText,
        position_details: document.querySelector(".pozisyon-bilgileri").innerText,
        statistics: document.querySelector(".istatistikler").innerText,
        factory_details: factory_details
    }
}

window.clickLink = () => {
    if (
        typeof (window.reg.link_index) != 'undefined'
        && window.reg.link_index < window.reg.links.length
    ) {
        window.reg.links[window.reg.link_index].click()
        window.reg.link_index += 1
        return true
    } else {
        return false
    }
}

window.regLinks = () => {
    // Linkleri alma
    links = document.querySelectorAll("a.link.position")

    // Linkleri saklama
    window.reg.links = links
    window.reg.link_index = 0 // TODO Debug için kullanılabilir
}

window.checkIfLinkChanged = () => {
    return document.getElementById("ilan0").innerText
}

window.nextPage = () => {
    const next_button = document.querySelector("a#lnkNextPage.nav.next")
    if (next_button.className.includes("disabled")) {
        return false
    } else {
        next_button.click()
        return true
    }
}


/*
"GENEL NİTELİKLER

Mart 2000 yılında Kore’de kurulan Netmarble mobil ve PC online oyun yayıncılığı ve Free to Play iş modelinin Dünya’daki öncüsüdür. Dünyanın en büyük online oyun pazarlarından biri olan Kore’de 35 milyon üzerindeki üyesi ile en büyük oyun portallarından da birisidir. Dünya Mobil oyun pazarının gelişiminde de birçok yeniliğe ilk olarak Netmarble imza atmıştır. Gelir olarak Kore’nin 1, Dünyanın ise 3. En büyük mobil oyun geliştiricisi ve yayıncısıdır.

Kore dışında, Japonya, Tayvan, Çin, Tayland, Endonezya ve Amerika’da da ofisleri bulunan Netmarble, 2013 yılında Türkiye ve Ortadoğu bölgesinin lider online oyun firması Joygame’i de bünyesine katarak global büyüme vizyonunu sağlamlaştırmıştır. Küçükyalı merkezimizde çalışacak aşağıda verilen özelliklere uygun “Dönemsel Proje Asistanı" aramaktayız.

Üniversite son sınıf öğrencisi
İyi seviyede İngilizce bilen
Oyun sektörüne ilgisi olan
İletişim becerileri gelişmiş
Takım çalışmasına yatkın
Haftanın en az 3 günü ofiste olabilecek
Müşteri ilişkileri ve operasyona destek verebilecek."
*/


/*
"Aday Kriterleri

Tecrübe:

Tecrübesiz adaylar

Eğitim Seviyesi:

Üniversite(Öğrenci)

Yabancı Dil:

İngilizce( Okuma : İyi, Yazma : İyi, Konuşma : İyi)"
*/


/*
"Pozisyon Bilgileri

Firma Sektörü:

Hizmet

Çalışma Şekli :

Sürekli / Tam zamanlı

Pozisyon Seviyesi:

Stajyer

Personel Sayısı:

1

Ülke/Şehir:

İstanbul(Asya)(Maltepe)"
*/


/*
"3
gün

639
görüntülenme

0-50
başvuru

22 April 2019 tarihinde güncellendi - 17 June 2019 tarihinde kapatılacaktı
*/

/*

"Firma Sektörü:

Hizmet

Çalışma Şekli:

Haftaiçi 09.00 - 18.00

Daha Fazla Bilgi

Sosyal / Yan Haklar:

Özel Sağlık Sigortası
Yemek Kartı (Ticket, Multinet, Sodexo vb.)
"

*/
































