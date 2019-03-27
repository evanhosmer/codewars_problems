def fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        lst = fib(n-1)
        lst.append(lst[-1] + lst[-2])
        return lst

def perimeter(n):
    lst = fib(n + 1)

    return 4 * sum(lst)

if __name__ == '__main__':
    print(perimeter(5))
    print(perimeter(7))
    print(perimeter(20))
    print(perimeter(30))
    print(perimeter(100))
