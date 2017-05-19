if __name__ == '__main__':
    l = int(input())
    r = int(input())
    max = 0
    for i in range(l, r + 1):
        for j in range(l, r + 1):
            # bi = bin(i)[2:]
            # bi = (8 - len(bi)) * '0' + bi
            # bj = bin(j)
            # bj = (8 - len(bj)) * '0' + bi
            # rta = ''.join(int(a, 2) ^ int(b, 2))[2:] for a, b in zip(bi, bj)
            # int(bin(3 ^ 10), 2)
            # print(rta)
            rta = int(bin(i^j), 2)
            if rta > max:
                max = rta

            # print("i: ", i, "j: ", j, ' = ', bi, bj, rta)


    print(max)
