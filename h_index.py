def solution(citations):
    answer = 0
    citations.sort()
    for i in range(len(citations)):
        if len(citations)-i>=citations[i]:
            answer=citations[i]
        else:
            if answer<len(citations)-i:
                answer=len(citations)-i
    return answer