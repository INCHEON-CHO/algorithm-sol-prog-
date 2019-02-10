def solution(brown, red):
    s = brown+red
    for i in range(1,red+1):
        if red%i==0:
            if s==(i+2)*(red/i+2):
                return [red/i+2, i+2]