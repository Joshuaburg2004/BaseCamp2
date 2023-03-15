temperatures = (
    ('1995', '3',
     ['47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5', '41.6', '43.2', '46.2', '45.8', '44.9', '39.4',
      '40.5', '42.0', '46.5', '46.2', '43.3', '41.7', '40.7', '39.6', '44.2', '47.8', '45.9', '47.3', '39.8', '35.2',
      '38.5', '40.5', '47.0']),
    ('2010', '3',
     ['39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2', '32.3', '33.3', '37.3', '39.9', '40.8', '42.9',
      '42.7', '42.6', '44.8', '50.3', '52.2', '55.2', '47.2', '45.0', '48.6', '55.0', '57.4', '50.9', '48.6', '46.2',
      '49.6', '50.1', '43.6']),
    ('2020', '3',
     ['43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9', '46.6', '50.5', '51.5', '47.7', '44.7', '44.0',
      '48.9', '45.3', '46.6', '49.7', '47.2', '44.8', '41.8', '40.9', '41.0', '42.7', '43.4', '44.0', '46.4', '45.5',
      '40.7', '39.5', '40.6'])
)


def q1(y):
    a = set(temperatures[0][2])
    b = set(temperatures[y][2])
    j = len(a.intersection(b))
    return j


def q3():
    d = {}
    for i in range(0, 3):
        highest = 0
        for item in temperatures[i][2]:
            item = float(item)
            if item > highest:
                highest = item
                d[i] = highest
    if d[0] > d[1] and d[0] > d[2]:
        return '1995'
    if d[1] > d[2] and d[1] > d[0]:
        return '2010'
    else:
        return '2020'


def q4():
    a = temperatures[0][2]
    b = temperatures[1][2]
    c = temperatures[2][2]
    a_sum = 0
    b_sum = 0
    c_sum = 0
    for i in a:
        i = float(i)
        a_sum += i
    for j in b:
        j = float(j)
        b_sum += j
    for k in c:
        k = float(k)
        c_sum += k
    a_avg = a_sum / 31
    b_avg = b_sum / 31
    c_avg = c_sum / 31
    if a_avg > b_avg and a_avg > c_avg:
        return '1995'
    if b_avg > a_avg and b_avg > c_avg:
        return '2010'
    else:
        return '2020'


def main():
    a = q1(1)
    b = q1(2)
    c = q3()
    d = q4()
    print(a)
    print(b)
    print(c)
    print(d)


if __name__ == '__main__':
    main()