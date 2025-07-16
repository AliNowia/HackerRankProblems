def count_substring(string, sub_string):
    n, m = len(string), len(sub_string)
    st, e, score = 0, m, 0
    while e <= n:
        if string[st: e] == sub_string:
            score += 1
        st, e = st+1, e+1
    return score
        
