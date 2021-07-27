# import
import random
def iterate(times=10000, children=10, min_score=10, alter=25):
    # define things used for agents
    n = min_score * children
    data = {} # where all the agents will be stored
    names = ["Zeus", "Poseidon", "Hestia", "Hermes", "Hera", "Hephaestus", "Hades", "Dionysus", "Demeter", "Athena", "Artemis", "Ares", "Apollo", "Aphrodite"]
    scores = []
    winINFO = {}
    for i in range(n): # stores all random agents in data with random values
        data[i] = {
            "data": {
            "score": random.randint(0, 100), # like this
            },
            "name": random.choice(names) # and this
        }
    t = 0
    # define things used for agents
    for i in range(times):
        winners = [] # reset winners
        for k, v in data.items(): # find average
            scores.append(v["data"]["score"])
        for item in list(data.values()): # for each agent, add their score to winners
            winners.append(item["data"]["score"])
        winners = sorted(winners)[-min_score:] # set winners to only the best of the old winners
        data = {} # kill all agents
        itn = 1
        for v in winners: # and replace them with new children
            itn += 1
            for i in range(children): # for the amount of kids each surviving agent gets
                data[max(list(data.keys()) + [0]) + 1] = { # redefine data correctly and store it in a new key
                "data": {
                "score": (v + random.randint(-alter, alter)), # alter score a little bit
                },
                "name": random.choice(names) # new name
            }
        t += 1
        print(str(round(t / times * 100, 3)) + "%, iter nr. " + str(t)) # give the percentage of progress
    return {"avg": sum(scores) / len(scores), "data": data}
# this last part is an example
def example(): # and it just gets the highest from 15 15gen 2child generations
    print(iterate(100000, 20, 5, 25)["avg"])
example()