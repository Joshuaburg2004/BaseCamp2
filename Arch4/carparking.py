import datetime
import sys
import os
import sqlite3


machine_dict = {}
class ParkedCar:
    def __init__(self, license_plate = '', check_in = datetime.datetime.now(), check_out = None, parking_fee = 2.5):
        self.license_plate = license_plate
        self.check_in = check_in
        self.check_out = check_out
        self.parking_fee = parking_fee


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
        self.car_list = []
        self.db_conn = sqlite3.connect(os.path.join(sys.path[0], 'carparkingmachine.db'))
        self.db_conn.execute('''CREATE TABLE IF NOT EXISTS parkings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_parking_machine TEXT NOT NULL,
                license_plate TEXT NOT NULL,
                check_in TEXT NOT NULL,
                check_out TEXT DEFAULT NULL,
                parking_fee NUMERIC DEFAULT 0);''')
        cur = self.db_conn.cursor()
        cur.execute('SELECT * FROM parkings WHERE car_parking_machine = ?', (self.id,))
        data = cur.fetchall()
        for tup in data:
            if tup[4] != None:
                continue
            self.check_in(tup[2], tup[3], tup[4])
        self.db_conn.commit()


    def check_in(self, license_plate, check_in = datetime.datetime.now(), check_out = None):
        capacity = self.capacity
        Car = ParkedCar(license_plate, check_in)
        parked_cars = self.parked_cars
        if len(parked_cars) >= capacity:
            return False
        if check_out == None:
            for car_dict2 in self.car_list:
                if license_plate in car_dict2.values():
                    return False
        self.car_list.append({"license_plate": Car, "check_in": Car.check_in})
        parked_cars[license_plate] = Car
        self.parked_cars = parked_cars
        for car_dict in self.car_list:
            if type(car_dict['check_in']) == str:
                self.db_conn.execute('''INSERT OR IGNORE INTO parkings (car_parking_machine, license_plate, check_in) VALUES (?, ?, ?)''', (self.id, car_dict["license_plate"].license_plate, car_dict["check_in"]))
            else:
                self.db_conn.execute('''INSERT OR IGNORE INTO parkings (car_parking_machine, license_plate, check_in) VALUES (?, ?, ?)''', (self.id, car_dict["license_plate"].license_plate, car_dict["check_in"].strftime('%d-%m-%Y %H:%M:%S')))
        self.db_conn.commit()
        return True
    

    def check_out(self, license_plate, check_out=datetime.datetime.now()):
        hourly_rate = self.hourly_rate
        parked_cars = self.parked_cars
        for car_dict in self.car_list:
            if license_plate == car_dict["license_plate"].license_plate:
                if type(car_dict["check_in"]) == str:
                    check_in = datetime.datetime.strptime(car_dict["check_in"], "%d-%m-%Y %H:%M:%S")
                else:
                    check_in = car_dict['check_in']
                result = (round((check_out - check_in) / datetime.timedelta(hours=1)) + 1) * hourly_rate
                if result >= 24 * hourly_rate:
                    result = 24 * hourly_rate
                for i in self.car_list:
                    if i['license_plate'].license_plate == license_plate:
                        if type(i['check_in']) == datetime:
                            self.db_conn.execute('''UPDATE parkings SET (check_out, parking_fee) = (?, ?) WHERE license_plate = ?''', (check_out.strftime('%d-%m-%Y %H:%M:%S'), result, license_plate))
                        else:
                            self.db_conn.execute('''UPDATE parkings SET (check_out, parking_fee) = (?, ?) WHERE license_plate = ?''', (check_out, result, license_plate))
                        self.car_list.remove(i)
                        break
                parked_cars.pop(license_plate)
                self.parked_cars = parked_cars
                for car_dict in self.car_list:
                    if type(car_dict['check_in']) == str:
                        self.db_conn.execute('''INSERT OR IGNORE INTO parkings (car_parking_machine, license_plate, check_in) VALUES (?, ?, ?)''', (self.id, car_dict["license_plate"].license_plate, car_dict["check_in"]))
                    else:
                        self.db_conn.execute('''INSERT OR IGNORE INTO parkings (car_parking_machine, license_plate, check_in) VALUES (?, ?, ?)''', (self.id, car_dict["license_plate"].license_plate, car_dict["check_in"].strftime('%d-%m-%Y %H:%M:%S')))
                self.db_conn.commit()
                return result
        print('Error: car not found')
    

    def get_parking_fee(self, license_plate):
        Car = self.parked_cars[license_plate]
        check_out = datetime.datetime.now()
        check_in = Car.get_check_in()
        result = (round((check_out - check_in) / datetime.timedelta(hours=1)) + 1) * self.hourly_rate
        if result >= 24 * self.hourly_rate:
            result = 24 * self.hourly_rate 
        return result


def main():
    car = ParkedCar('12-aa-12', )
    cpm = CarParkingMachine('North', 10, 2.5, {car.license_plate: car})
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
            if a is not True and a is not False:
                print(a)
            if a is True:
                print('license registered')
        elif Input == 'o':
            car_inp = input('License: ')
            result = str(cpm.check_out(license_plate=car_inp))
            if result != 'None':
                if result[2] != '0':
                    result = float(result)
                    print(f'parking fee: {result:.2f} EUR')
                else:
                    result = float(result)
                    print(f'parking fee: {result:.1f} EUR')


if __name__ == '__main__':
    main()