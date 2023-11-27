# Odoo 17 CE E-commerce Image Fetcher Deployment Guide

This guide will walk you through the steps to deploy the `odoo_image_fetcher` module in a production environment.

## Prerequisites

- Odoo 17 CE installed and running
- Access to the Odoo server (SSH access for command line)

## Steps

1. **Upload the Module**

    Transfer the `odoo_image_fetcher` module directory to the Odoo server. The module should be placed in the addons directory of your Odoo installation.

    ```
    scp -r odoo_image_fetcher user@yourserver:/path/to/odoo/addons/
    ```

2. **Update Module List**

    Log in to your Odoo instance as an administrator. Navigate to `Apps > Update Apps List`. Click on `Update`.

3. **Install the Module**

    In the Apps menu, remove the 'Apps' filter and search for `odoo_image_fetcher`. Click on `Install`.

4. **Configure the Module**

    After installation, go to `Settings > Technical > Database Structure > Models` and search for `product.template`. You should see new fields `main_image_url` and `extra_media_urls`. These fields can be used to input the URLs for main product images and extra media.

5. **Restart the Server**

    Restart the Odoo server to apply the changes.

    ```
    sudo service odoo restart
    ```

6. **Verify the Installation**

    To verify the installation, navigate to any product on your e-commerce site. You should see the main product image and extra media fetched from the URLs you provided.

## Troubleshooting

If you encounter any issues during the deployment, please refer to the Odoo logs located at `/var/log/odoo/odoo-server.log`.

## Support

For additional support, please refer to the `README.md` file in the `odoo_image_fetcher` module directory or contact the module developer.