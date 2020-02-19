def binaryGap(N):
    if N <= 4:
        return 0
    length = 0
    head = 0
    tail = 1
    bin_n = str(bin(N)).replace('0b','')
    while tail < len(bin_n):
        if bin_n[tail] == '0':#string
            tail += 1
        elif bin_n[tail] == '1':
            if tail-head -1 > length:
                length = tail - head - 1
                head = tail
                tail += 1
            else:# tail-head+1 <= lenth
                head = tail
                tail += 1

    return length


def toBin(n):
    return bin(n).replace('0b','')

print(binaryGap(9))
print(bin(9))
