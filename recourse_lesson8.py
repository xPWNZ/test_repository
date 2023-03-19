def gen_bin(N:int, M:int, prefix =None):
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        gen_bin(N,M-1,prefix)
        prefix.pop()

gen_bin(4,3)