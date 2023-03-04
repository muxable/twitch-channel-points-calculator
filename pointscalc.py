# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#print("Hello world")

import sys
import argparse



def pointsdelta(startingPoints, watchTime, tier, activeWatching):
    # multiplier for each tier
    tier0 = float(1)
    tier1 = float(1.2)
    tier2 = float(1.4)
    tier3 = float(2.0)
    
    # divide without remainder 
    watchCountedMultiplier = watchTime // 5
    # extensions exist to auto redeem otherwise need to click button
    activeMultiplier = watchTime // 15
    
    # current values for points
    watching = 10
    activeWatch = 50
    

    # activeWatching take in 0 for not active redeeming, 1 for active redeeming
    newPoints = (watching*watchCountedMultiplier) + (activeWatch*activeMultiplier*activeWatching) # change 1 to active watching boolean flag
    
    # multiply points based on tiers
    if (tier == 0):
        newPoints = newPoints * tier0
    elif (tier == 1):
        newPoints = newPoints * tier1
    elif (tier == 2):
        newPoints = newPoints * tier2
    elif (tier == 3):
        newPoints = newPoints * tier3
    
    # add new points to original points
    totalpoints = startingPoints + newPoints
    return int(totalpoints)
    
print(pointsdelta(100, 15, 2, 0))  


parser = argparse.ArgumentParser(description='Calculate twitch points given a starting value and ')


# to do
# need to add boolean for active watching instead of assuming zero
# input santization
# flags logic
# unit tests
