def flexagon(_n):
    if _n == 1:
        return 1
    return 2 * flexagon(_n - 1) + 1


def flexagon_iterative(_n):
    _sum = 1
    for i in range(2, _n + 1):
        _sum = 2 * _sum + 1
    return _sum


while True:
    n = int(input("需要对折次数："))
    if n == 0:
        break
    print("纸上会有{}条折痕".format(flexagon(n)))
    # print(flexagon_iterative(n))
