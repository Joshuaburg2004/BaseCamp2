class Car:
    def __init__(self, brand, color, model, price, sold_to='', sold=False):
        self.brand = brand
        self.color = color
        self.model = model
        self.price = price
        self.sold = sold
        self.sold_to = sold_to

    def sell(self, name):
        self.sold = True
        customer = name
        self.sold_to = customer
        return

    def print(self):
        print(f'brand: {self.brand}')
        print(f'color: {self.color}')
        print(f'model: {self.model}')
        print(f'price: {self.price}')
        if self.sold:
            print(f'Sold to: {self.sold_to.get_name()}')
            return
        print('Not sold yet')
        return


class Motorcycle:
    def __init__(self, brand, color, model, price, sold_to='', sold=False):
        self.brand = brand
        self.color = color
        self.model = model
        self.price = price
        self.sold = sold
        self.sold_to = sold_to

    def sell(self, name):
        self.sold = True
        customer = Customer(name)
        self.sold_to = customer
        return

    def print(self):
        print(f'brand: {self.brand}')
        print(f'color: {self.color}')
        print(f'model: {self.model}')
        print(f'price: {self.price}')
        if self.sold:
            print(f'Sold to: {self.sold_to.get_name()}')
            return
        print('Not sold yet')
        return


class Customer:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f'Name: {self.name}')

    def get_name(self):
        return self.name


def main():
    car_list = []
    car1 = Car('BMW', 'red', 'X5', 25000)
    car2 = Car('opel', 'black', 'astra', 10000)
    car3 = Car('mercedes', 'gray', 'gla', 20000)
    car4 = Car('kia', 'blue', 'stonic', 15000)
    car_list.append(car1)
    car_list.append(car2)
    car_list.append(car3)
    car_list.append(car4)
    customer1 = Customer('John Doe')
    customer2 = Customer('Joshua van der Burg')
    car_list[1].sell(customer1)
    car_list[3].sell(customer2)
    for p in car_list:
        p.print()


if __name__ == '__main__':
    main()
