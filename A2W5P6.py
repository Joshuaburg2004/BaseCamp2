def next_verse(x):
    x -= 1
    verses = ['A partridge in a pear tree',
              'Two turtledoves',
              'Three french hens',
              'Four calling birds',
              'Five gold rings (five golden rings)',
              'Six geese a-laying',
              'Seven swans a-swimming',
              'Eight maids a-milking',
              'Nine ladies dancing',
              'Ten lords a-leaping',
              'Eleven pipers piping',
              'Twelve drummers drumming']
    verse_numbers = ['1st',
                     '2nd',
                     '3rd',
                     '4th',
                     '5th',
                     '6th',
                     '7th',
                     '8th',
                     '9th',
                     '10th',
                     '11th',
                     '12th']
    print(f'On the {verse_numbers[x]} day of Christmas, my true love sent to me ', end='')
    if x == 0:
        print('A partridge in a pear tree')
    else:
        for i in range(0, x + 1):
            a = x - i
            if a > 0:
                if a == 1:
                    print(verses[a], end=' ')
                else:
                    print(verses[a], end=', ')
            else:
                print('And', verses[0])


if __name__ == '__main__':
    for i in range(1, 13):
        next_verse(i)