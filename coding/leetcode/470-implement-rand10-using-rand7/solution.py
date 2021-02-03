def rand10(self):
    f = lambda: rand7() + (rand7() - 1) * 7
    n = f()
    while n > 40:
        n = f()
    return n % 10 + 1
