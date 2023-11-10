inp = input().strip()
candidate = input().strip()


def check_anagram(inp, cand):
    i = sorted(inp)
    o = sorted(cand)
    if i == o:
        return 1
    return 0


print(check_anagram(inp, candidate))
