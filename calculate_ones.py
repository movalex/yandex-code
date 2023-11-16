inp = int(input())


def calculate_ones(qty):
    counter = 0
    max_number = 0
    for i in range(qty):
        num = int(input())
        if num == 1:
            counter += 1
            if max_number < counter:
                max_number = counter
        else:
            counter = 0

    return max_number


result = calculate_ones(inp)
print(result)
