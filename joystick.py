def solution(name):
    answer = 0
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(name)):
        if alpha.index(name[i])<=12:
            answer+=alpha.index(name[i])
        else:
            answer+=26-alpha.index(name[i])
    if 'A' not in name:
        answer+=len(name)-1
    else:
        cnt = name.count('A')
        while 1:
            if 'A'*cnt in name:
                break
            else:
                cnt-=1
        idx = name.index('A'*cnt)
        if cnt>=idx:
            answer+=2*len(name[:idx])
            answer+=len(name[cnt+idx+1:])-1
        else:
            answer+=len(name)-1
            
                
    return answer