    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        # find lowest score
        if score < lowest_score:
            lowest_score = score
        records.append([name, score])
         
    sec_lowest_score = 0
    d = 9999
    
    # find second lowest score
    for i in range(len(records)):
        dist = abs(lowest_score - records[i][1])
        if dist != 0 and dist < d:
            d = dist
            sec_lowest_score = records[i][1]
            
    # match students and sort them
    for i in range(len(records)):
        if records[i][1] == sec_lowest_score:
            studs.append(records[i][0])
    studs.sort()
    for n in studs:
        print(n)
