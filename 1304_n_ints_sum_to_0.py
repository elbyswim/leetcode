def sumZero(n: int):
    if n == 1:
        return [0]
    elif n % 2 == 0:
        return [x + 1 for x in range(n // 2)] + [-x - 1 for x in range(n // 2)]
    else:
        return [0] + [x + 1 for x in range(n // 2)] + [-x - 1 for x in range(n // 2)]