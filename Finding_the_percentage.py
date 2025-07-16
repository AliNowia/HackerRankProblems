if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    avg = 0
    summ = 0
    n = len(student_marks[query_name])
    for s in student_marks[query_name]:
        summ = summ + s
    avg = float(summ/n)
    
    print(f'{avg:.2f}')
