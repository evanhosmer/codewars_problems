def dirReduc(arr):
    opppairs = {"NORTH":1, "SOUTH":-1, "WEST":-2, "EAST":2}

    while True:
        n = 0
        for i in range(len(arr)-1):
            if opppairs[arr[i]]+opppairs[arr[i+1]] == 0:
                del arr[i]
                del arr[i]
                n += 1
                break
        if n == 0:
            return arr

if __name__ == '__main__':
    t1 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    t2 = ["NORTH", "WEST", "SOUTH", "EAST"]
    print(dirReduc(t1), dirReduc(t2))
