import requests
from bs4 import BeautifulSoup
import fake_useragent

class Shop:
    def __init__(self, url, count):
        self.url = url
        self.count = count
        self.arr = []
        self.headers = {
            'user-agent': fake_useragent.UserAgent().random
        }

    def get_catalog(self, container_selector, item_selector, name_selector, price_selector):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
        except requests.RequestException:
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        container = soup.select_one(container_selector)
        if not container:
            return []

        items = container.select(item_selector)
        for item in items:
            name_elem = item.select_one(name_selector)
            price_elem = item.select_one(price_selector)
            if name_elem and price_elem:
                self.arr.append((name_elem.text.strip(), price_elem.text.strip()))

        return self.arr

    def get_one(self, container_selector, name_selector, price_selector):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
        except requests.RequestException:
            return None, None

        soup = BeautifulSoup(response.content, 'html.parser')
        container = soup.select_one(container_selector)
        if not container:
            return None, None

        name = soup.select_one(name_selector).text.strip() if soup.select_one(name_selector) else None
        price_elem = container.select_one(price_selector)
        price = price_elem.text.strip() if price_elem else None

        return name, price

class ApStore(Shop):
    def __call__(self):
        if self.count == 1:
            return self.get_one(
                '.shop_product_wrapper.clearfix',
                'h1[data-product]',
                '.single_product_price_con.clearfix.test ins'
            )
        else:
            return self.get_catalog(
                '.products_filter.clearfix',
                '.add2cart_slide',
                '.add2cart_prod_name',
                '.add2cart_prod_price'
            )

class Biggeek(Shop):
    def __call__(self):
        if self.count == 1:
            return self.get_one(
                '.prod-info',
                'h1',
                '.total-prod-price'
            )
        else:
            return self.get_catalog(
                '.catalog-content__page',
                '.catalog-card',
                '.catalog-card__title.cart-modal-title',
                '.cart-modal-count'
            )


apstore = ApStore('https://ap-store.ru/products/apple-iphone-11-64-gb-chernyj',1)
apstore2 = ApStore('https://ap-store.ru/products/air-pods-pro-2-go-pokoleniya',1)
apstore3 = ApStore('https://ap-store.ru/catalog/iphone-15-pro-max',0)
print(apstore())
print(apstore2())
print(apstore3())

biggeek = Biggeek('https://biggeek.ru/products/smartfon-apple-iphone-air-256-gb-cernyj-kosmos-space-black',1)
print(biggeek())
