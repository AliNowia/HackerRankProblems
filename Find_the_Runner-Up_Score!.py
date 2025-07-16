if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    max_score = max(scores)
    d = 201
    for s in scores:
        dist = abs(max_score - s)
        if dist != 0 and dist < d:
            d = dist
            runner_up = s
    print(runner_up)
