for a in range(19):
    for b in range(19):
        if (a % 19 == (4 * b) % 19) and (b % 19 == (5 * a) % 19):
            print((a, b, a + b, a + 2 * b, (6 * a) % 19 == (a + b) % 19, (6 * b) % 19 == (a + 2 * b) % 19))
