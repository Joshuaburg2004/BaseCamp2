import datetime


class ParkedCar:
    def __init__(self, license_plate = '', check_in = datetime.datetime.now()):
        self.license_plate = license_plate
        self.check_in = check_in
    

    def get_check_in(self):
        return self.check_in
    

    def get_license_plate(self):
        return self.license_plate


class CarParkingMachine:
    def __init__(self, capacity = 10, hourly_rate = 2.5, parked_cars={}):
        self.parked_cars = parked_cars
        self.capacity = capacity
        self.hourly_rate = hourly_rate
    

    def check_in(self, license_plate, check_in = datetime.datetime.now()):
        capacity = self.capacity
        Car = ParkedCar(license_plate, check_in)
        parked_cars = self.parked_cars
        if len(parked_cars) == capacity:
            return False
        parked_cars[license_plate] = Car
        self.parked_cars = parked_cars
        return True
    

    def check_out(self, license_plate, check_out=datetime.datetime.now()):
        hourly_rate = self.hourly_rate
        parked_cars = self.parked_cars
        if license_plate in parked_cars.keys():
            Car = parked_cars[license_plate]
            check_in = Car.get_check_in()
            result = (round((check_out - check_in)/datetime.timedelta(hours=1)) + 1) * hourly_rate
            if result >= 24 * hourly_rate:
                result = 24 * hourly_rate
            parked_cars.pop(license_plate)
            self.parked_cars = parked_cars
            return result
        else:
            print('Error: car not found')
    

    def get_parking_fee(self, license_plate):
        Car = self.parked_cars[license_plate]
        check_out = datetime.datetime.now()
        check_in = Car.get_check_in()
        result = (round((check_out - check_in)/datetime.timedelta(hours=1)) + 1) * self.hourly_rate
        if result >= 24 * self.hourly_rate:
            result = 24 * self.hourly_rate 
        return result


def main():
    cpm = CarParkingMachine(10, 2.5, )
    Input = ''
    while Input != 'q':
        Input = input('''[I] Check-in car by license plate
[O] Check-out car by license plate
[Q] Quit program\n''').lower()
        if Input == 'i':
            car_inp = input('License: ')
            a = cpm.check_in(license_plate=car_inp)
            if a is False:
                print('Capacity reached')
            else:
                print('license registered')
        elif Input == 'o':
            car_inp = input('License: ')
            result = str(cpm.check_out(license_plate=car_inp))
            if result[2] != '0':
                result = float(result)
                print(f'parking fee: {result:.2f} EUR')
            else:
                result = float(result)
                print(f'parking fee: {result:.1f} EUR')


if __name__ == '__main__':
    main()