def solve(s):
    ans = ""
    switch = True
    for c in s:
        if c == ' ':
            ans += c
            switch = True
        elif switch:
            ans += c.upper()
            switch = False
        else:
            ans += c
    return ans
    
