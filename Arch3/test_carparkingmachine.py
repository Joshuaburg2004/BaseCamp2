from carparking import CarParkingMachine
from datetime import datetime, timedelta

# Test for a normal check-in with correct result (True)
def test_check_in_capacity_normal():
    cpm = CarParkingMachine(10, 4, )
    Car = cpm.check_in('ah-435-h')
    assert Car is True
# Test for a check-in with maximum capacity reached (False)
def test_check_in_capacity_reached():
    cpm = CarParkingMachine(2, 4, {'a': 0, 'b': 1})
    Car = cpm.check_in('ah-435-h')
    assert Car is False
# Test for checking the correct parking fees
def test_parking_fee():
    # Assert that parking time 2h10m, gives correct parking fee
    # Assert that parking time 24h, gives correct parking fee
    # Assert that parking time 30h == 24h max, gives correct parking fee
    cpm = CarParkingMachine(10, 4, )
    cpm.check_in('ah-435-h', datetime.now()-timedelta(hours=2, minutes=10))
    cpm.check_in('bh-435-h', datetime.now()-timedelta(hours=24))
    cpm.check_in('ch-435-h', datetime.now()-timedelta(hours=30))
    assert cpm.get_parking_fee(cpm.parked_cars['ah-435-h'].get_license_plate(), ) == 12
    assert cpm.get_parking_fee(cpm.parked_cars['bh-435-h'].get_license_plate(), ) == 96
    assert cpm.get_parking_fee(cpm.parked_cars['ch-435-h'].get_license_plate(), ) == 96
# Test for validating check-out behaviour
def test_check_out():
    # Assert that {license_plate} is in parked_cars
    # Assert that correct parking fee is provided when checking-out {license_plate}
    # Assert that {license_plate} is no longer in parked_cars
    cpm = CarParkingMachine(10, 4, )
    cpm.check_in('ah-435-h', datetime.now()-timedelta(hours=2, minutes=10))
    assert 'ah-435-h' in cpm.parked_cars
    assert cpm.check_out('ah-435-h') == 12
    assert 'ah- 435-h' not in cpm.parked_cars