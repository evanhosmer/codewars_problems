import string
import re
def rot13(message):
    mess = []
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    for word in message.split(' '):
        newm = []
        for char in list(word):
            if char.isdigit() or re.match(r"[.~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]", char):
                newm.append(char)
            if char.isupper():
                if upper.find(char) <= 12:
                    newm.append(upper[upper.find(char) + 13])
                else:
                    newm.append(upper[(upper.find(char) + 13) - 26])
            elif char.islower():
                if lower.find(char) <= 12:
                    newm.append(lower[lower.find(char) + 13])
                else:
                    newm.append(lower[(lower.find(char) + 13) - 26])
        mess.append(''.join(newm))

    return ' '.join(mess)

if __name__ == '__main__':
    t1 = "test"
    t2 = "This is a test!"
    t3 = "10+3 is a test also!"
    print(rot13(t1),rot13(t2),rot13(t3))
