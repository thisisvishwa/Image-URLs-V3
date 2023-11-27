```python
from odoo.tests import HttpCase

class TestUI(HttpCase):

    def setUp(self):
        super(TestUI, self).setUp()
        self.product_template = self.env['product.template'].create({
            'name': 'Test Product',
            'main_image_url': 'http://example.com/main.jpg',
            'extra_media_urls': 'http://example.com/extra1.jpg,http://example.com/extra2.jpg'
        })

    def test_fetch_main_image(self):
        response = self.url_open('/shop/product/%s' % self.product_template.id)
        self.assertIn('http://example.com/main.jpg', response.text)

    def test_fetch_extra_media(self):
        response = self.url_open('/shop/product/%s' % self.product_template.id)
        self.assertIn('http://example.com/extra1.jpg', response.text)
        self.assertIn('http://example.com/extra2.jpg', response.text)

    def test_broken_url(self):
        self.product_template.write({
            'main_image_url': 'http://example.com/broken.jpg'
        })
        response = self.url_open('/shop/product/%s' % self.product_template.id)
        self.assertIn('placeholder.jpg', response.text)

    def test_invalid_url(self):
        self.product_template.write({
            'main_image_url': 'invalid_url'
        })
        response = self.url_open('/shop/product/%s' % self.product_template.id)
        self.assertIn('placeholder.jpg', response.text)
```