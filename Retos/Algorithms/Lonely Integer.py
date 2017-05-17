# Head ends here
def lonelyinteger(b):
    answer = ""
    lst = []
    for n in b:
        if n not in lst:
            lst.append(n)
        else:
            pos = lst.index(n)
            del lst[pos]

    if lst:
        answer = " ".join(lst)

    return answer


# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = input().strip().split(" ")
    print(lonelyinteger(b))
