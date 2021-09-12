# import
import random
import f
import time
import os
import json
def iterate(times=10000, children=10, min_score=1, alter=10000, logfreq=10, jsonlogfreq=10):
    # define things used for agents
    n = min_score * children
    logtime = 0
    loginfo = {}
    data = {} # where all the agents will be stored
    names = ["Zeus", "Poseidon", "Hestia", "Hermes", "Hera", "Hephaestus", "Hades", "Dionysus", "Demeter", "Athena", "Artemis", "Ares", "Apollo", "Aphrodite"]
    startup = time.time()
    for i in range(n): # stores all random agents in data with random values
        data[i] = {
            "data": {
            "score": random.randint(-alter, alter), # like this
            },
            "name": random.choice(names) # and this
        }
    t = 0
    # define things used for agents
    for i in range(times):
        scores = []
        winners = [] # reset winners
        for k, v in data.items(): # find average
            scores.append(v["data"]["score"])
        for item in list(data.values()): # for each agent, add their score to winners
            winners.append(item["data"]["score"])
        rated = f.rate(winners) # set winners to only the best of the old winners
        winners = rated["list"][-min_score:]
        avgdistance = rated["avgdistance"]
        data = {} # kill all agents
        itn = 1
        for v in winners: # and replace them with new children
            itn += 1
            for i in range(children): # for the amount of kids each surviving agent gets
                data[max(list(data.keys()) + [0]) + 1] = { # redefine data correctly and store it in a new key
                "data": {"score": (v + random.randint(-avgdistance, avgdistance)) # alter score a little bit
                    },
                "name": random.choice(names) # new name
            }
        timerec = time.time()
        
        t += 1
        log = t % logfreq == 0 or t == times
        jsonlog = t % jsonlogfreq == 0 or t == times
        if log:
            os.system('cls' if os.name=='nt' else 'clear')
            print(f"{str(round(t / times * 100, 3))}%\niter nr.  {str(t)}\nest. time: {round(((time.time() - startup) / t) * (times - t), 2)} seconds\ntime passed: {round(time.time() - startup, 2)} seconds\ntime spent logging: {round(logtime, 2)} seconds\naverage distance: {str(round(avgdistance))}\ncurrent average: {sum(scores) // len(scores)}\ncurrent best: {winners[-1]}\nbest found: {str(avgdistance == 0)}") # give the percentage of progress
        timerec = time.time() - timerec
        logtime += timerec
        if jsonlog:
            loginfo[t] = {
                "progress": t / times,
                "time left": ((time.time() - startup) / t) * (times - t),
                "time passed": time.time() - startup,
                "time spent logging": logtime,
                "time per iteration": (time.time() - startup) / t,
                "average distance": avgdistance,
                "average": sum(scores) // len(scores),
                "best": winners[-1],
                "item found": avgdistance == 0
            } 
    return loginfo
# this last part is an example
def example(): # and it just gets the highest from 15 15gen 2child generations
    with open("log.json", "w") as f:
        json.dump(iterate(10000, 10, 1, 10000, 10000, 1), f, indent=4)
example()
input()