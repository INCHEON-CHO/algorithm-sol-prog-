def solution(baseball):
    answer = 0
    bl=[]
    for i in range(123,988):
        ob = str(i)
        if '0' in ob:
            continue
        ob = set(list(ob))
        if len(ob)==3:
            bl.append(str(i))
    for i in bl:
        cnt=0
        for j in range(len(baseball)):
            ball=0
            strike=0
            a = str(baseball[j][0])
            for k in range(3):
                if i[k] in a and i[k]==a[k]:
                    strike+=1
                elif i[k] in a and i[k]!=a[k]:
                    ball+=1
            if strike!=baseball[j][1] or ball!=baseball[j][2]:
                break
            else:
                cnt+=1
            if cnt==len(baseball):
                answer+=1
    return answer