import math

def brute_force(growth_rates):
    t = 0
    while (True):
        users = 0.0
        for rate in growth_rates:
            users += rate ** t
        if users > 1e9: break
        t += 1
    return t

def get_upper_limit(growth_rates):
    min_rate = min(growth_rates)
    return math.log(1e9, min_rate)

def get_population(growth_rates, time):
    users = 0.0
    for rate in growth_rates:
        users += rate ** time
    return users

def efficient_search(growth_rates):
    low = 0
    high = get_upper_limit(growth_rates)
    population = 0
    while low <= high:
        mid = (low + high) / 2
        population = round(get_population(growth_rates, time=mid), 0)
        if population == 1e9: return mid
        if population < 1e9: low = mid
        elif population > 1e9: high = mid

def getBillionUsersDay(growthRates):
    return math.ceil(efficient_search(growthRates))

print(getBillionUsersDay([1.5]))