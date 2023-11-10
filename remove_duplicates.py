inp = int(input())


def remove_duplicates(inp: int):
    seen = []
    for i in range(inp):
        num = int(input())
        if not num in seen:
            seen.append(num)
    for result in seen:
        print(result)


inp = int(input())


def remove_duplicates(inp: int) -> dict:
    seen = set()
    for i in range(inp):
        num = int(input())
        if not num in seen:
            seen.add(num)
            yield num


inp = int(input())
seen = remove_duplicates(inp)
for result in seen:
    print(result)


def remove_duplicates(inp: int) -> dict:
    seen = set()
    while inp > 0:
        num = input()
        if not num in seen:
            seen.add(num)
            yield num
        inp -= 1


inp = int(input())

inputs = [int(input()) for _ in range(inp)]


def remove_duplicates(n, *inputs):
    unique_inputs = []
    seen = set()
    for i in range(n):
        if inputs[i] not in seen:
            unique_inputs.append(inputs[i])
            seen.add(inputs[i])
    return list(unique_inputs)


unique_inputs = remove_duplicates(inp, *inputs)

for num in unique_inputs:
    print(num)


inp = int(input())

inputs = [int(input()) for _ in range(inp)]


def remove_duplicates(n, *inputs):
    """checks if next input is not equal to the previous then adds the number ro result list"""
    unique_inputs = []
    if n > 0:
        unique_inputs.append[inputs[0]]
    for i in range(1, n):
        if inputs[i] != inputs[i - 1]:
            unique_inputs.append(inputs[i])
    return list(unique_inputs)


unique_inputs = remove_duplicates(inp, *inputs)

for num in unique_inputs:
    print(num)

inp = int(input())

inputs = [int(input()) for _ in range(inp)]


def remove_duplicates(n, *inputs):
    """checks if next input is not equal to the previous then adds the number ro result list"""
    if n > 0:
        print(inputs[0])
    for i in range(1, n):
        if inputs[i] != inputs[i - 1]:
            print(inputs[i])


unique_inputs = remove_duplicates(inp, *inputs)
