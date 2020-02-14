def isAnagram(s,t):
    if len(s) != len(t):
        return False
    else:
        match = [i for i in s]
        for char in t:
            if char in match:
                match.remove(char)
        if len(match) == 0:
            return True
        else:
            return False

s = "anagram"
t = "nagarak"
print(isAnagram(s,t))
