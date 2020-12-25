# BoGo Sort Python Module | Python3 | Mehmet Yilmaz | 3-22-2020

import random
import time

# color classes for coloring terminal output
class colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# main bogo sort function:
#   bogosort(list, False, False) = only return sorted list.
#   bogosort(list, True, True) = return sorted list, # Tries, RunTime, & every attempt.
#   bogosort(list, True, False) = return sorted list, # Tries, & RunTime
def bogosort(l, entireSet, allAttempts):
    start_time = time.time()
    tries = 0
    attempts = []
    while((all(l[i] <= l[i+1] for i in range(len(l)-1))) != True):
        tries = tries + 1
        if(allAttempts): attempts.append(l)
        random.shuffle(l)
    runTime = (time.time() - start_time) # secs
    if(entireSet and allAttempts): return l, tries, runTime, attempts
    elif(entireSet): return l, tries, runTime
    else: return l

# bogosort example:
#   bogo sort a list of 0-size and print out data/results
def bogoExample(size):
    exlist = list(range(0, size))
    random.shuffle(exlist)
    print(colors.UNDERLINE + "BoGo Sort → O((n+1)!)" + colors.END)
    print("Unsorted: " + str(exlist))
    ans = bogosort(exlist, True, False)
    print("  Sorted: " + str(ans[0]))
    print(" # Tries: " + str(("{:,}".format(ans[1]))))
    return " RunTime: " + str(ans[2]) + " secs"
    

