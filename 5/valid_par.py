from collections import Counter
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

if __name__ == '__main__':
    t1 = "hi())("
    t2 = "hi(hi)()"
    print(valid_parentheses(t1))
    print(valid_parentheses(t2))
