def solution(n, words):
    a,b=0,0
    for i in range(len(words)-1):
        if len(words[i])==1:
            a = i%n + 1
            b = i//n + 1
            break
        elif words[i+1] in words[:i+1]:
            a = (i+1)%n + 1
            b = (i+1)//n + 1
            break
        elif words[i][-1]!=words[i+1][0]:
            a = (i+1)%n + 1
            b = (i+1)//n + 1
            break
    return [a,b]