def reverse_alternate(string):
    l = string.split(' ')
    newl = []
    for idx,word in enumerate(l):
        if not idx % 2 == 0:
            newl.append(word[::-1])
        else:
            newl.append(word)

    return ' '.join(newl)



if __name__ == '__main__':
    print(reverse_alternate("Did it work?"))
