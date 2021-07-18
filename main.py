# import
import random
# create random agents
# # define things used for agents
n = 5
data = {} # where all the agents will be stored
names = ["Zeus", "Poseidon", "Hestia", "Hermes", "Hera", "Hephaestus", "Hades", "Dionysus", "Demeter", "Athena", "Artemis", "Ares", "Apollo", "Aphrodite"]
average = 0
scores = []
winners = {}
for i in range(n): # stores all random agents in data with random values
            data[i] = {
                "data": {
                "score": random.randint(0, 100), # like this
                },
                "name": random.choice(names) # and this
            }
def iterate(times=15, amountproduce=2):
    global data
    global scores
    global winners
    t = 0
    for i in range(times):
        for k, v in data.items(): # find average
            scores.append(v["data"]["score"])
        for k, v in data.items(): # now that we found average, we can eliminate and reproduce agents.
            if v["data"]["score"] > sum(scores) / len(scores): # if above average, reproduce.
                winners[k] = v
        data = {} # kill all agents
        itn = 1
        for k, v in winners.items(): # and replace them with new children
            itn += 1
            for i in range(amountproduce): # for the amount of kids each surviving agent gets
                data[max(list(data.keys()) + [0]) + 1] = { # redefine data correctly and store it in a new key
                "data": {
                "score": (v["data"]["score"] + random.randint(-25, 25)), # alter score a little bit
                },
                "name": random.choice(names) # new name
            }
        t += 1
        print(str(int(t / times * 100)) + "%, iter nr. " + str(t)) # give the percentage of progress
    return [sum(scores) / len(scores), data]
# loop
print(iterate(20, 2))