import datetime
import json
import os
import sys
import csv
from carparking import ParkedCar, CarParkingMachine


def report():
    inputter = input("Give location to report: ")
    name, time_1, time_2 = inputter.split(',')
    car_list = take_from_json(name)
    datetime_1 = datetime.datetime.strptime(time_1, "%d-%m-%Y")
    datetime_2 = datetime.datetime.strptime(time_2, "%d-%m-%Y")
    try:
        for car_dict in car_list:
            for car in car_dict.values():
                time = car.check_in
                if datetime_1 < time < datetime_2:
                    write_to_csv(name, time)
    except TypeError:
        return


def write_to_csv(name, write):
    with open(os.path.join(sys.path[0], f'parkedcars_{name}_from_10-11-2022_to_12-11-2022.csv'), 'w',newline='', encoding='UTF-8') as f:
        writer = csv.writer(f)
        writer.writerow('license_plate;check_in;check_out;parking_fee')
        writer.writerows(write)


def take_from_json(name):
    car_list = []
    json_file = f'{name}_state.json'
    try:
        with open(os.path.join(sys.path[0], json_file), 'r', encoding='UTF-8') as f:
            for car_dict in json.load(f):
                car_dict['license_plate'] = ParkedCar(car_dict["license_plate"], datetime.datetime.strptime(car_dict['check_in'], '%d-%m-%Y %H:%M:%S'))
                car_list.append(car_dict)
            return car_list
    except FileNotFoundError:
        return


def main():
    inputter = input('''[P] Report all parked cars during a parking period for a specific parking machine
[F] Report total collected parking fee during a parking period for all parking machines
[Q] Quit program\n''').upper()
    if inputter == 'P':
        report()
    if inputter == 'Q':
        sys.exit()


if __name__ == '__main__':
    main()