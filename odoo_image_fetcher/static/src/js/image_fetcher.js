odoo.define('odoo_image_fetcher.image_fetcher', function (require) {
    "use strict";

    var ajax = require('web.ajax');

    function fetchImage(url, elementId) {
        ajax.jsonRpc("/image_fetcher/fetch", 'call', { 'url': url })
            .then(function (data) {
                if (data.success) {
                    document.getElementById(elementId).src = data.image_url;
                } else {
                    document.getElementById(elementId).src = "/odoo_image_fetcher/static/src/img/placeholder.png";
                }
            });
    }

    function fetchMainImage(mainImageUrl) {
        fetchImage(mainImageUrl, "main-image");
    }

    function fetchExtraMedia(extraMediaUrls) {
        extraMediaUrls.forEach(function (url, index) {
            fetchImage(url, "extra-media-" + index);
        });
    }

    return {
        fetchMainImage: fetchMainImage,
        fetchExtraMedia: fetchExtraMedia
    };
});