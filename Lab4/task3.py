import constMod as cM
def energy(high = 1, mass = 1, speed = 1):
    return(mass*speed**2/2) + mass * cM.g * high
print(energy(cM.high, cM.m, cM.v))
