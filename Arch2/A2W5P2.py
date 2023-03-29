def calculate_fare(distance):
    base = 4.00
    dist = 0.25
    distance = float(distance)
    return base + dist * (distance // 0.140 + (distance % 0.140 > 0))


if __name__ == "__main__":
    distance = input("Distance traveled: ")
    fare = calculate_fare(distance)
    print(fare)