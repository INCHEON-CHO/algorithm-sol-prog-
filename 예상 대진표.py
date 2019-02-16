def solution(n,a,b):
    answer = 0
    while 1:
        answer+=1
        if abs(a-b)==1:
            if a<b and a%2!=0:
                break
            elif a>b and b%2!=0:
                break
        a=a//2+a%2
        b=b//2+b%2
    return answer