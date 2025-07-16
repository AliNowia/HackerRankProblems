# MANY TEST CASES FAILED DUE TO TIME OUT
# NEEDS OPTIMIZATION
def minion_game(s):
    N = len(s)
    vowels, checked = ['A', 'E', 'I', 'O', 'U'], []
    s_score, k_score, l = 0, 0, 0
    while l < N:
        for i in range(N):
            st, e = l, i+l
            ss = s[st:e+1]
            while e <= N-1:
                if s[st:e+1] == ss and s[st:e+1] not in checked:
                    if s[st] in vowels:
                        k_score += 1
                    else:
                        s_score += 1
                st, e = st+1, e+1
            if ss not in checked:
                checked.append(ss)
        l+=1
    if s_score > k_score:
        print(f"Stuart {s_score}")
    elif k_score > s_score:
        print(f"Kevin {k_score}")
    else:
        print("Draw")
