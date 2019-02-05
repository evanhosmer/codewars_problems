def order_weight(strng):
    '''
    Weight == Sum of digits in number
    When two numbers have the same "weight", let us class them as if they were strings and not numbers:
    100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since,
    having the same "weight" (9) it comes before as a string.
    '''
    sums = []
    nums = strng.split(' ')
    for num in nums:
        sum_digits = sum(int(y) for y in num if y.isdigit())
        sums.append((num,sum_digits))

    new = sorted(sums,key = lambda x: (x[1],x[0]))
    final = ' '.join([x[0] for x in new])

    return final

if __name__ == '__main__':
    print(order_weight("103 123 4444 99 2000"))
    print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
