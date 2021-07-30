import math
def rate(l):
    scores = {}
    num = 246341
    for i in l:
        if i == 0:
            scores[i] = num
        else:
            scores[i] = math.sqrt((i - num)**2)
    return {"avgdistance": sum(list(scores.values())) // len(scores), "list": list(list({k: v for k, v in sorted(scores.items(), key=lambda item: item[1])}.keys())[::-1])}