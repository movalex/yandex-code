import time


def timing(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        result = t2 - t1
        print(f"Func {func.__name__} took {result:.9f} sec.")
        return res

    return wrapper


def generate_parentheses1(n):
    """the slowest"""
    if n == 0:
        return [""]
    result = []
    for i in range(n):
        left = generate_parentheses1(i)

        right = generate_parentheses1(n - i - 1)

        for l in left:
            for r in right:
                result.append("(" + l + ")" + r)
    return sorted(result)


@timing
def run_gen1(n):
    generate_parentheses1(n)


run_gen1(14)


@timing
def generate_parentheses2(n):
    output = []

    def rec(left, right, stack, candidate):
        if left == right == 0:
            output.append(candidate)
            return
        if left > 0:
            rec(left - 1, right, stack + 1, candidate + "(")
        if right > 0 and stack > 0:
            rec(left, right - 1, stack - 1, candidate + ")")

    rec(n, n, 0, candidate="")
    return output


g = generate_parentheses2(15)


@timing
def generate_parentheses3(n) -> None:
    out = []

    def run(current: str, opened: int, closed: int, n: int):
        if len(current) == 2 * n:
            out.append(current)
            return
        if opened < n:
            run(current + "(", opened + 1, closed, n)
        if closed < opened:
            run(current + ")", opened, closed + 1, n)

    run("", 0, 0, n)
    return out


g = generate_parentheses3(14)
print(len(g))


res = []


def generate_parentheses4(current: str, opened: int, closed: int, n: int):
    """just printout algorithm"""
    if len(current) == 2 * n:
        res.append(current)
        return
    if opened < n:
        generate_parentheses4(current + "(", opened + 1, closed, n)
    if closed < opened:
        generate_parentheses4(current + ")", opened, closed + 1, n)


@timing
def run_gen4(n):
    generate_parentheses4("", 0, 0, n)


run_gen4(3)
print(len(res))
