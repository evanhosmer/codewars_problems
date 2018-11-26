from collections import Counter
import numpy as np
def move_zeros(array):
    if sum(1 for item in array if item == 0 and type(item) == int or type(item) == float) == 0:
        return array
    else:
        n = len(array)
        newl = [num for num in array if num != 0 or type(num) == bool]
        zeros = sum(1 for item in array if item == 0 and type(item) == int or type(item) == float)
        l2 = [0] * zeros
        newl[n - 1:] = l2
        return newl


if __name__ == '__main__':
    t1 = [1,2,0,1,0,1,0,3,0,1]
    t2 = [9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]
    t3 = ["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]
    t4 = ["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]
    res1 = move_zeros(t1)
    res2 = move_zeros(t2)
    print(move_zeros(t3))
