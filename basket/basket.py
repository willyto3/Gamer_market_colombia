class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.basket

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total