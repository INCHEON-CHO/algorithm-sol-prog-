import math
def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)-1):
            for k in range(j+1,len(nums)-1):
                s = nums[i]+nums[j+1]+nums[k+1]
                if s%2!=0:
                    for l in range(3,s):
                        if s%l==0:
                            break
                        if l>math.sqrt(s):
                            answer+=1
                            break
    return answer