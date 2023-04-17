class Converter:
    def __init__(self, amount=0, typed=''):
        self.amount = amount
        self.type = typed

    def inches(self):
        my_dict = {'inches': 1, 'feet': 12, 'yards': 36, 'miles': 63360, 'kilometers': 39370, 'meters': 39.37,
                'centimeters': 0.3937, 'millimeters': 0.03937}
        res = self.amount * my_dict[self.type]
        print(res)
        return res

    def feet(self):
        my_dict = {'inches': 1/12, 'feet': 1, 'yards': 3, 'miles': 5280, 'kilometers': 3280.84, 'meters': 3.28084,
                   'centimeters': 0.0328084, 'millimeters': 0.00328084}
        res = self.amount * my_dict[self.type]
        print(res)
        return res

    def yards(self):
        my_dict = {'inches': 1 / 36, 'feet': 1 / 3, 'yards': 1, 'miles': 1760, 'kilometers': 1093.61, 'meters': 1.09361,
                   'centimeters': 0.0109361, 'millimeters': 0.00109361}
        res = self.amount * my_dict[self.type]
        print(res)
        return res

    def miles(self):
        my_dict = {'inches': 1 / 63360, 'feet': 1 / 5280, 'yards': 1 / 1760, 'miles': 1, 'kilometers': 1 / 1.609, 'meters': 1 / 1609,
                   'centimeters': 1 / 160900, 'millimeters': 1 / 1609000}
        res = self.amount * my_dict[self.type]
        print(res)
        return res

    def kilometers(self):
        my_dict = {'meters': 1000, 'centimeters': 100000, 'millimeters': 1000000, 'kilometers': 1,
                   'miles': 1.609, 'yards': 1 / 1093.61, 'feet': 1 / 3280.84, 'inches': 1 / 39370}
        res = self.amount * my_dict[self.type]
        print(res)
        return res

    def meters(self):
        my_dict = {'meters': 1, 'centimeters': 100, 'millimeters': 1000, 'kilometers': 1 / 1000,
                   'miles': 1.609 / 1000, 'yards': (1 / 1093.61) / 1000, 'feet': (1 / 3280.84) / 1000, 'inches': (1 / 39370) / 1000}
        res = self.amount * my_dict[self.type]
        print(res)
        return res

    def centimeters(self):
        my_dict = {'meters': 1 / 100, 'centimeters': 1, 'millimeters': 10, 'kilometers': 1 / 100000,
            'miles': 1.609 / 100000, 'yards': (1 / 1093.61) / 100000, 'feet': (1 / 3280.84) / 100000, 'inches': (1 / 39370) / 100000}
        res = self.amount * my_dict[self.type]
        print(res)
        return res

    def millimeters(self):
        my_dict = {'meters': 1 / 1000, 'centimeters': 0.1, 'millimeters': 1, 'kilometers': 1 / 1000000,
                   'miles': 1.609 / 1000000, 'yards': (1 / 1093.61) / 1000000, 'feet': (1 / 3280.84) / 1000000,
                   'inches': (1 / 39370) / 1000000}
        res = self.amount * my_dict[self.type]
        print(res)
        return res


if __name__ == '__main__':
    c = Converter(5, 'meters')
    c.feet()