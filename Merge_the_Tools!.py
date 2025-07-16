# RUNTIME ERROR AT TEST CASES 14,15
# NEEDS OPTIMIZATION

def is_in(c, s):
    for l in s:
        if l == c:
            return True
    return False
    
def merge_the_tools(string, k):
    n = len(string)
    t = []
    st, e = 0, k
    
    if k > 1:
        for i in range(int(n/k)):
            t.append(string[st:e])
            st=e
            e = e + k
            
        for u in range(len(t)):
            temp = ""
            for i in range(0, len(t[u])):
                if is_in(t[u][i], temp):
                    continue
                temp = temp + t[u][i]
            t[u] = temp
    else:
        t = [c for c in s]
        
    for i in range(len(t)):
        print(t[i])
