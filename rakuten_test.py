from itertools import permutations

def solution(s):
    if len(s) <= 1:
        return 0
    dict_v = list('AEOIU')
    dict_c = list('QWRTYPSDFGHJKLZXCVBNM')
#print(len(dict_c)+len(dict_v))

#print(dict_v)
#print(dict_c)
    words = [''.join(c) for c in permutations(s)]
    words = set(words)

    useless = set()
    for word in words:
        for i in range(0,len(word),2):
            if word[i] not in dict_c or word[i+1] not in dict_v:
                useless.add(word)
    left = words - useless
    print(left)
    print(len(left))

#解法二：求除有多少个不同的元音和多少个不同的辅音，然后排列组合。


s = 'CATE'
solution(s)
