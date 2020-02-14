from itertools import permutations

def solution(s):

    if len(s) <= 1:
        return 0

   # 创建字典
    dict_v = list("AEIOU")
    dict_c = list("QWRTYPSDFGHJKLZXCVBNM")

    #全排列
    #words = [''.join(c) for c in permutations(s)]
    words = [''.join(c) for c in permutations(s)]
    print(words)
    words = set(words)
    #print(len(words), len(set(words)) )
    ret = words.copy()

    #删除不正确的项目
    for word in words:
        #con
        for i in range(0, len(word), 2):
            if word[i] not in dict_c:
                ret.remove(word)
                break
        #vowel
    words = ret.copy()
    for word in words:
         for j in range(1, len(word), 2):
            if word[j] not in dict_v:
                 ret.remove(word)
                 break

    return len(ret)

s = 'BAAR'
solution(s)
