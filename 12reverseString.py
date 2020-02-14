def reverseString(s):
    head = 0
    tail = len(s) -1
    while head < tail:
        s[head],s[tail] = s[tail],s[head]
        head += 1
        tail -= 1
    return s

def reverseString_2(s):
    s.reverse()
    return s

s = ["h","e","l","l","o"]
print(reverseString_2(s))

