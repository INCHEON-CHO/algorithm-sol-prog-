def solution(people,limit):
    people.sort()
    length=len(people)
    light=0
    heavy=length-1
    count=0
    while(light<heavy):
        if people[light]+people[heavy]<=limit:
            count+=1
            light+=1
            heavy-=1
        else:
            heavy-=1
    return length-count