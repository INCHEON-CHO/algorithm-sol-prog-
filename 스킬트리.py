def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        sk = ""
        for j in range(len(i)):
            if i[j] in skill:
                sk+=i[j]
        if skill.find(sk)==0:
            answer+=1
    return answer