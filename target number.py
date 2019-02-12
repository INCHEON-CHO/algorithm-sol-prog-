def solution(numbers, target):
    answer = 0
    result=[numbers[0],-numbers[0]]
    numbers.pop(0)
    while numbers:
        stack=[]
        n = numbers.pop(0)
        for i in result:
            stack.append(i+n)
            stack.append(i-n)
        result=stack[:]
    return result.count(target)