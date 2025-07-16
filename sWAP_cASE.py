def swap_case(s):
    ans = ""
    for l in s:
        if not ord(l) in [x for x in range(65, 91, 1)] and not ord(l) in [x for x in range(97, 123, 1)]:
            ans = ans + l
        elif ord(l) in [x for x in range(97, 123)]:
            ans = ans + chr(ord(l) - 32)
        else:
            ans = ans + chr(ord(l) + 32)
    return ans
