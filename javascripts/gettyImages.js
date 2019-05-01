window.getCurrentPageImgUrls = () => {
    // Url dizisi
    const urls = [];

    // Url'leri tek tek alma
    const figureCollection = document.getElementsByTagName("figure");
    for (let i = 0; i < figureCollection.length; i++) {
        const figure = figureCollection[i];
        const url = figure.getElementsByTagName("img")[0].src

        // Url metin ise ekleme
        if (typeof url == 'string') {
            urls.push(url);
        }
    }

    return urls;
};

// Sonraki sayfaya geçme
window.nextPage = () => {
    document.getElementById("next-gallery-page").click();
};

return getCurrentPageImgUrls();
