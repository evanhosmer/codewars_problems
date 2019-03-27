import re
def inc_str(s):
    if s == '':
        return '1'

    if s.isalpha():
        return s + '1'

    digits = re.findall(r'\d+', s)[-1]
    num = int(re.findall(r'\d+', s)[-1])
    numnew = num + 1
    zeros = digits.replace(str(num), '').count('0') - (len(str(numnew)) - len(str(num)))

    if digits[0] != '0':
        return s.replace(digits, '{}'.format(numnew))

    if all(char == '0' for char in digits):
        leadz = '0' * (len(digits) - 1)
        return s.replace(digits,leadz + '{}'.format(numnew))

    else:
        leadzero = '0' * zeros
        return s.replace(digits,leadzero + '{}'.format(numnew))

if __name__ == '__main__':
    print(inc_str('foobar23'))
    print(inc_str('foobar0099'))
    print(inc_str('foobar0045'))
    print(inc_str("foobar00"))
    print(inc_str('foobar0101'))
