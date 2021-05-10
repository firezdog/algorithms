def bruteForce(growthRates):
    t = 0
    while (True):
        users = 0.0
        for rate in growthRates:
            users += rate ** t
        if users > 1e9: break
        t += 1
    return t

def getBillionUsersDay(growthRates):
    return bruteForce(growthRates)

print(getBillionUsersDay([1.01,1.02]))