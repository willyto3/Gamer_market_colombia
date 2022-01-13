from store.models import Product
from decimal import Decimal


class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            self.session['skey'] = {}
        self.basket = basket

    def add(self, product, product_qty):
        product_id = product.id
        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(
                product.price), 'product_qty': int(product_qty)}

        self.session.modified = True

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product
        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = Decimal(item['price']*item['product_qty'])
            yield item

    def __len__(self):
        return sum(item['product_qty'] for item in self.basket.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['product_qty'] for item in self.basket.values())
