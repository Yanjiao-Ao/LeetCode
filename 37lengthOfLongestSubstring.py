def lengthOfLongestSubstring(s):#特殊情况：为空 ''，只有空格' '
    maxlenth = -1
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    for head in range(len(s)):
        hash = {}
        for tail in range(head,len(s)):
            if s[tail] not in hash:
                hash[s[tail]] = 1
            else:
                break
            if len(hash) > maxlenth:
                maxlenth = len(hash)
    return maxlenth


s = 'abcabcbb'
s1 = 'bbbbbbbb'
s2 = 'pwwkew'
s3 = 'au'
print(lengthOfLongestSubstring(s3))
