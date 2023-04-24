import datetime
import sys
import os


machine_dict = {}


class CarParkingLogger:
    def __init__(self, id, logger = 'carparklog.txt'):
        self.id = id
        self.logger = logger
        self.logger_list = []
        with open(os.path.join(sys.path[0], logger)) as f:
            for line in f:
                self.logger_list.append(line)


    def get_machine_fee_by_day(self, car_parking_machin_id: str, search_date: str):
        search_date_edit = datetime.datetime.strptime(search_date, '%d-%m-%Y')
        cpm = machine_dict[car_parking_machin_id]
        total = 0
        for action in cpm.logger:
            action1 = action.split(' ')
            action2 = action1[1].split(';')
            if action1[0] == search_date_edit:
                cpm = machine_dict[car_parking_machin_id]
                total += cpm.hourly_rate * ((datetime.datetime(hour=24) - action2[0]) / datetime.timedelta(hours=1))
        return total


    def get_total_car_fee(self, license_plate):
        total = 0
        for cpm in machine_dict.values():
            parked_cars = cpm.parked_cars
            for car in parked_cars:
                if license_plate == car.get_license_plate():
                    total += cpm.get_parking_fee(license_plate)
        return total


    def send_to_file(self, time = datetime.datetime.now().replace(microsecond=0).strftime('%d-%m-%Y %H:%M:%S'), license_plate='', action='', parking_fee=None):
        with open(os.path.join(sys.path[0], self.logger), 'w') as file:
            if parking_fee == None:
                file.write(f'{time};cpm_name={self.id};license_plate=[{license_plate}];action={action}')
            else:
                file.write(f'{time};cpm_name={self.id};license_plate=[{license_plate}];action={action};parking_fee={int(parking_fee)}')


class ParkedCar:
    def __init__(self, license_plate = '', check_in = datetime.datetime.now()):
        self.license_plate = license_plate
        self.check_in = check_in
    

    def get_check_in(self):
        return self.check_in
    

    def get_license_plate(self):
        return self.license_plate


class CarParkingMachine:
    def __init__(self, id = 0, capacity = 10, hourly_rate = 2.5, parked_cars={}):
        self.parked_cars = parked_cars
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.id = id
        cpl = CarParkingLogger(self.id)
        self.logger = cpl


    def check_in(self, license_plate, check_in = datetime.datetime.now()):
        capacity = self.capacity
        Car = ParkedCar(license_plate, check_in)
        parked_cars = self.parked_cars
        if len(parked_cars) >= capacity:
            return False
        parked_cars[license_plate] = Car
        self.parked_cars = parked_cars
        self.log(None, check_in, license_plate, 'check-in')
        return True
    

    def check_out(self, license_plate, check_out=datetime.datetime.now()):
        hourly_rate = self.hourly_rate
        parked_cars = self.parked_cars
        if license_plate in parked_cars.keys():
            Car = parked_cars[license_plate]
            check_in = Car.get_check_in()
            result = (round((check_out - check_in) / datetime.timedelta(hours=1)) + 1) * hourly_rate
            if result >= 24 * hourly_rate:
                result = 24 * hourly_rate
            parked_cars.pop(license_plate)
            self.parked_cars = parked_cars
            self.log(result, check_in, license_plate, 'check-out')
            return result
        else:
            print('Error: car not found')
    

    def get_parking_fee(self, license_plate):
        Car = self.parked_cars[license_plate]
        check_out = datetime.datetime.now()
        check_in = Car.get_check_in()
        result = (round((check_out - check_in) / datetime.timedelta(hours=1)) + 1) * self.hourly_rate
        if result >= 24 * self.hourly_rate:
            result = 24 * self.hourly_rate 
        return result


    def take_from_file(self, file):
        with open(file, 'r') as f:
            content = f.readlines()
            for line in content:
                check_in, _, license_plate, _ = line.split(';')
                car = license_plate.split('=')[1]
                self.parked_cars[car] = check_in
    

    def log(self, parking_fee: int, time=datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'), license_plate='', action=''):
        if parking_fee == None:
            self.logger.send_to_file(time, license_plate, action)
        else:
            self.logger.send_to_file(time, license_plate, action, parking_fee)


def main():
    cpm = CarParkingMachine(None, 10, 2.5, )
    machine_dict[cpm.id] = cpm
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