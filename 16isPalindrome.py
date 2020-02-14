def isPalindrome(s):
    if s == None:
        return True
    list = [str for str in s.lower() if str.isalnum() == True]
    #print(list)
    #print(len(list))
    i = 0
    j = len(list) -1
    while i < j:
        if list[i] == list[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

s1 = "race a car"
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s1))

