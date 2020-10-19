# Packages and Modules Used:
from itertools import permutations # used for finding permutations
import time # used to get function run time
import math

# Nearest Neighbor Function - First Attempt (DOES NOT WORK...)
# - Does not work for most case(s), the correct NN is below this one
def NearestNeighbor(allPointsNow):
    # copy allPointsNow to prevent removing of indexs on the orignal
    allPoints = allPointsNow.copy()

    p = allPoints[0] # p = p_0
    i = 0 # i = 0

    visited = [] # store visted points
    visited.append(p) # add initial points to visted
    distance = 0 # store total distance traveled between all points

    # While there are still unvisited points, keep traveling
    while(len(allPoints) > 0):
        i = i + 1
        x = i

        lowIndex = len(allPoints) - 1 # grab last index from allPoints
        # find distance with point distance formula (d=root(dx^2-dy^2)
        low = 0 # stores shortest travel distance
        low = float(allPoints[lowIndex][0]-p[0])**2 + float(allPoints[lowIndex][1]-p[1])**2

        # while there are still unvisited points
        while(x < len(allPoints)):
            # find distance with point distance formula (d=root(dx^2-dy^2)
            v = float(allPoints[x][0]-p[0])**2 + float(allPoints[x][1]-p[1])**2

            # if low is not defined, set first index distance as the first low
            if(low == 0):
                low = v
                lowIndex = x
            else:
                # set low and lowIndex to a new shorter distance
                if(v < low and v != 0):
                    low = v
                    lowIndex = x # stores index of point with lowest travel distance
            x = x + 1

        distance = distance + float((low)**(1/2)) # adds to total distance
        p = allPoints[lowIndex] # select p_i to be the closest unvisited point to p_i-1
        visited.append(p) # add new point to visited list
        allPoints.pop(lowIndex) # remove visited point from allPoints

    print(distance) # display distance traveled
    print(visited) # display visited path

# CORRECT Nearest Neighbor Function- O(n^2)
def nn(allPointsNow):
    allPoints = allPointsNow.copy()

    visited = []

    p = allPoints[0]
    visited.append(p)

    allPoints.pop(0)

    totalD = 0

    while(allPoints):
        lowIndex = 0
        low = 0

        for i in range(len(allPoints)):
            v = math.sqrt((allPoints[i][0]-p[0])**2 + float(allPoints[i][1]-p[1])**2)
            if(low == 0 and i == 0):
                low = v
                lowIndex = i
            elif(v < low):
                low = v
                lowIndex = i

        totalD = totalD + low
        p = allPoints[lowIndex]
        visited.append(p)
        allPoints.pop(lowIndex)

    p = visited[0]
    last = len(visited)-1
    v = float(visited[last][0]-p[0])**2 + float(visited[last][1]-p[1])**2
    v = float((v)**(1/2))
    totalD = totalD + v
    visited.append(visited[0])

    print(totalD)
    print(visited)

# OptimalTSP Function - O(n!*n)
def OptimalTSP(allPoints):
    # get all permutation from allPoints using itertools package's permutations module
    perm = permutations(allPoints)

    # Convert perm from turple to list of list of lists
    allPermutation = []
    for i in list(perm):
        k = list(i)
        k.append(k[0])
        allPermutation.append(k) # add starting point to path

    shortestDistance = 0 # hold shortest distance for a path
    shortestPath = [] # hold shortest possible path from the permutations

    # for each of the n! permutations of allPoints_i of point set P
    # loop though every path and path's points in allPoints
    for i in range(len(allPermutation)):
        totalDistance = 0 # store current path distance
        for p in range(len(allPermutation[i])-1):
            # find distance with point distance formula (d=root(dx^2-dy^2)
            d = ((allPermutation[i][p+1][0]-allPermutation[i][p][0])**2 + (allPermutation[i][p+1][1]-allPermutation[i][p][1])**2)**(1/2)
            totalDistance = totalDistance + d
        # add current path if its shorter then the previous shortest path
        if(shortestDistance == 0 or totalDistance < shortestDistance):
            shortestDistance = totalDistance
            shortestPath = allPermutation[i]

    print(shortestDistance) # display distance traveled
    print(shortestPath) # display visited path

# reads given text file format and returns a list of lists data structure
def getData(address):
    final = []
    size = 0 # n size
    point = [] # list of a point

    with open(address) as f:
        i = 0
        for lines in f:
            if(i == 0):
                size = int(lines)
            else:
                s = lines.find(' ')
                point.append(int(lines[:s]))
                point.append(int(lines[(s+1):]))
                final.append(point)
                point = []
            i = i + 1
    return final

# main function for nearest neighbors
def main_Neareest_Neighbors(final):
    print()
    print("Nearest Neighbor Results:")
    start_time = time.time() # start timer
    #NearestNeighbor(final) # failed attempt
    nn(final)
    print("%s seconds " % (time.time() - start_time)) # end timer
    print()

# main function for optimal TSP
def main_optimal_TSP(final):
    print("Optimal TSP Results:")
    start_time = time.time() # start timer
    OptimalTSP(final)
    print("%s seconds " % (time.time() - start_time)) # end timer
    print()

def main(data):
    ### Run Nearest Neighbor:
    main_Neareest_Neighbors(data)

    ### Run Optimal TSP:
    main_optimal_TSP(data)

if __name__ == "__main__":
    # generated random data from: https://www.random.org/integer-sets/
    # Enter desired data text file here:
    data = getData("data9.txt")

    main(data)