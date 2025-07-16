# TEST_CASE 15 IS WRONG ANSWER. I don't remember why.

def is_in(c, s):
    for l in s:
        if l == c:
            return True
    return False
    
def merge_the_tools(string, k):
    n = len(string)
    t = []
    st, e = 0, k

    for i in range(int(n/k)):
        if i > n-(n/k):
            break
        t.append(string[st:e])
        st=e
        e = e + k

    for k in range(len(t)):
        temp = ""
        for i in range(0, len(t[k])):
            if is_in(t[k][i], temp):
                continue
            temp = temp + t[k][i]
        t[k] = temp
        temp = ""
    
    for i in range(len(t)):
        print(t[i])
