import re
def change(s, prog, version):
    '''
    A valid phone format is +1-xxx-xxx-xxxx, where each x is a digit.
    If the phone number is valid, replace it with "+1-503-555-0090"
    '''
    vers = re.findall("\d+\.\d+",s)
    if len(vers) == 0:
        return 'ERROR: VERSION or PHONE'
    else:
        sversion = vers[0]
    if len(sversion.split('.')) != 2:
        return 'ERROR: VERSION or PHONE'
    if sversion.split('.')[0] == '':
        return 'ERROR: VERSION or PHONE'
    if sversion != '2.0':
        v = version
    else:
        v = '2.0'
    phonenumber = s.split('\n')[3][7:]
    pattern = re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE)
    if len(phonenumber) != 15:
        return 'ERROR: VERSION or PHONE'
    if phonenumber[0:3]!= '+1-':
        return 'ERROR: VERSION or PHONE'
    if pattern.match(phonenumber[3:]) is None:
        return 'ERROR: VERSION or PHONE'
    else:
        phonenum = "+1-503-555-0090"

    return 'Program: {} Author: g964 Phone: {} Date: 2019-01-01 Version: {}'.format(prog,phonenum,v)


    if __name__ == '__main__':
        s1 = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-0091\nDate: Tues April 9, 2005\nVersion: 6.7\nLevel: Alpha'
		s11 = 'Program title: Hammer\nAuthor: Tolkien\nCorporation: IB\nPhone: +1-503-555-0090\nDate: Tues March 29, 2017\nVersion: 2.0\nLevel: Release'
		s12 = 'Program title: Primes\nAuthor: Kern\nCorporation: Gold\nPhone: +1-503-555-009\nDate: Tues April 9, 2005\nVersion: 6.7\nLevel: Alpha'

        Test.assert_equals(change(s1, 'Ladder', '1.1'), 'Program: Ladder Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 1.1')
		Test.assert_equals(change(s11, 'Balance', '1.5.6'), 'Program: Balance Author: g964 Phone: +1-503-555-0090 Date: 2019-01-01 Version: 2.0')
		Test.assert_equals(change(s12, 'Ladder', '1.1'), 'ERROR: VERSION or PHONE')
