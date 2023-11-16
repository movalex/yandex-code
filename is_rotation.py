def is_rotation(a,b):
    if len(a) != len(b):
        return False
    a_first = a[0]
    b_index = -1
    for i in range(len(b) - 1):
        if b[i] == a_first:
            b_index = i
            break
    if b_index == -1:
        return False
    for n, elem in enumerate(a):
        # use mod (%) to scroll index
        second_index = (b_index + n) % len(a)
        if b[second_index] != elem:
            return False
    return True

list1 = [1,2,3,4,5,6,7]
list2 = [7,1,2,3,4,5,6]

print(is_rotation(list1, list2))
