```python
from odoo.tests import common

class TestProductTemplate(common.TransactionCase):

    def setUp(self):
        super(TestProductTemplate, self).setUp()
        self.product_template = self.env['product.template']

    def test_fetch_main_image(self):
        product = self.product_template.create({
            'name': 'Test Product',
            'main_image_url': 'http://example.com/image.jpg',
        })
        self.assertEqual(product.main_image_url, 'http://example.com/image.jpg')

    def test_fetch_extra_media(self):
        product = self.product_template.create({
            'name': 'Test Product',
            'extra_media_urls': 'http://example.com/media.jpg',
        })
        self.assertEqual(product.extra_media_urls, 'http://example.com/media.jpg')

    def test_broken_url(self):
        product = self.product_template.create({
            'name': 'Test Product',
            'main_image_url': 'http://brokenurl.com/image.jpg',
        })
        self.assertNotEqual(product.main_image_url, 'http://brokenurl.com/image.jpg')

    def test_invalid_url(self):
        product = self.product_template.create({
            'name': 'Test Product',
            'main_image_url': 'invalidurl',
        })
        self.assertNotEqual(product.main_image_url, 'invalidurl')
```