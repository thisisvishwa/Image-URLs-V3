```python
from odoo import http
from odoo.http import request
import requests
import asyncio

class MainController(http.Controller):

    @http.route('/fetch_main_image', type='json', auth='public')
    async def fetch_main_image(self, **kwargs):
        product_id = kwargs.get('product_id')
        product = request.env['product.template'].browse(product_id)
        main_image_url = product.main_image_url

        try:
            response = requests.get(main_image_url)
            response.raise_for_status()
        except (requests.HTTPError, requests.ConnectionError):
            return '/path/to/default/placeholder/image'

        return response.content

    @http.route('/fetch_extra_media', type='json', auth='public')
    async def fetch_extra_media(self, **kwargs):
        product_id = kwargs.get('product_id')
        product = request.env['product.template'].browse(product_id)
        extra_media_urls = product.extra_media_urls

        extra_media_content = []
        for url in extra_media_urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                extra_media_content.append(response.content)
            except (requests.HTTPError, requests.ConnectionError):
                extra_media_content.append('/path/to/default/placeholder/image')

        return extra_media_content
```