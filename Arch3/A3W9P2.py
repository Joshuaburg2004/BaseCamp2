class Product:
    def __init__(self, name='', amount=0, price=1.00):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, amount):
        if amount < 10:
            total = self.price * amount
        if 99 >= amount >= 10:
            total = self.price * amount * 0.9
        if amount > 99:
            total = self.price * amount * 0.8
        return total

    def make_purchase(self, amount):
        prod_amount = self.amount
        if prod_amount >= amount:
            self.amount = prod_amount - amount
            return self.amount
        else:
            amount = prod_amount
            self.amount = 0
            print(f'We only have {amount} of {self.name}. Your amount has been adjusted')
            return amount


def main():
    prod = Product('Apple', 10, 5)
    print(prod.get_price(5))
    print(prod.make_purchase(5))


if __name__ == '__main__':
    main()
