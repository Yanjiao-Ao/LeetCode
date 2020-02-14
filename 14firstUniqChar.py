def firstUniqChar(s):
    hashmap = {}
    uniq = []
    #build hashmap
    for i in s:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] += 1

    for j in hashmap:
        if hashmap[j] == 1:
            uniq.append(j)
    if len(uniq) == 0:
        return -1
    else:
        for i in range(len(s)):
            if uniq[0] == s[i]:
                return i

s = 'loveleetcodevtc'
print(firstUniqChar(s))
