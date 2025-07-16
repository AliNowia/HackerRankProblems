if __name__ == '__main__':
    # 1 1 2 3
    x = int(input())  # i
    y = int(input())  # j
    z = int(input())  # k
    n = int(input())  # n != i + j + k
    i = [n for n in range(0, x+1)] # [0, 1]
    j = [n for n in range(0, y+1)] # [0, 1]
    k = [n for n in range(0, z+1)] # [0, 1, 2]
    cords = [[i[a], j[b], k[c]] for a in range(len(i)) for b in range(len(j)) for c in range(len(k)) if i[a] + j[b] + k[c] != n]
    print(cords)
