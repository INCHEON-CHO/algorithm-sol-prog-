def solution(numbers):
    a = sorted(numbers, key=lambda x:str(x)*4 if len(str(x))==1 else(str(x)*2 if len(str(x))==2 else(str(x)+str(x)[0] if len(str(x))==3 else str(x))),reverse=True)
    answer=list(map(str,a))
    if len(answer)==answer.count('0'):
        return '0'
    return "".join(answer)