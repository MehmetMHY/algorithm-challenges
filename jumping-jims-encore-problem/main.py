import matplotlib.pyplot as plt # using matplotlib for displaying graph
import networkx as nx # using NetworkX to create, manage, and search though graph

def readFile(fileName): # reads text file lines into list
    x = list()
    with open(fileName) as f:
      for line in f:
        x.append(line.replace('\n', '').split())
    return x

def createValueMatrix(x): # creates matrix of cell values
    y = []
    for i in range(len(x)):
        point = [] ; pz = [] ; start = len(x[0])*i
        for p in range(len(x[i])):
            point.append(int(x[i][p]))
        y.append(point)
    return y

def createIndexMatrix(row, col): # creates matrix of cell indexes (1-row*col)
    z = [] ; q = 0 ; point = []
    for i in range(row*col):
        q = q + 1
        point.append(q)
        if(len(point) % col == 0):
            z.append(point)
            point = []
    return z

def readData(fileName): # main function creating matrices, row, and col values
    x = readFile(fileName) # read text file into list
    y = createValueMatrix(x) # covert list of lines into a matrix of values

    row = y[0][0] # get matrix row
    col = y[0][1] # get matrix col
    y.pop(0)

    z = createIndexMatrix(row, col) # creates matrix of cell indexes (1-row*col)

    return y, z, row, col

def makePath(e, s, t): # convert NetworkX's output into a single list
    ans = []
    ans.insert(0, t)
    while(t != s):
        for i in range(len(e)):
            if(e[i][1] == t):
                ans.insert(0, e[i][0])
                t = e[i][0]
    return ans

def finalAnswer(n, answer): # convert single list output into the required format
    for i in range(len(n)):
        value = abs(n[i])
        for x1 in range(row):
            for y1 in range(col):
                if(z[x1][y1] == value):
                    answer = answer + "(" + str(x1+1) + ", " + str(y1+1) + ") "
    return answer

y, z, row, col = readData("input.txt") # read and create variables for desired file

G = nx.DiGraph() # set NetworkX graph object

# generate over all graph
for i in range(row):
    for p in range(col):
        point = z[i][p] # correct cell index
        v = abs(y[i][p]) # value in the cell
        sv = 1 # used to invert node value if that node is a Red

        # check every vertical and horizontal axis, then adds that cell(s) as an edge
        if(i+v >= 0 and i+v < row):
            if(y[i+v][p] < 0): sv = -1
            G.add_edge(point, z[i+v][p]*sv)
        sv = 1
        if(i-v >= 0 and i-v < row):
            if(y[i-v][p] < 0): sv = -1
            G.add_edge(point, z[i-v][p]*sv)
        sv = 1
        if(p+v >= 0 and p+v < col):
            if(y[i][p+v] < 0): sv = -1
            G.add_edge(point, z[i][p+v]*sv)
        sv = 1
        if(p-v >= 0 and p-v < col):
            if(y[i][p-v] < 0): sv = -1
            G.add_edge(point, z[i][p-v]*sv)

        # check every diagonal axis, then adds that cell(s) as an edge
        sv = 1
        point = z[i][p]*-1
        v = abs(y[i][p])
        if(i+v >= 0 and i+v < row and p+v >= 0 and p+v < col):
            if(y[i+v][p+v] < 0): sv = -1
            G.add_edge(point, z[i+v][p+v]*-1*sv)
        sv = 1
        if(i-v >= 0 and i-v < row and p-v >= 0 and p-v < col):
            if(y[i-v][p-v] < 0): sv = -1
            G.add_edge(point, z[i-v][p-v]*-1*sv)
        sv = 1
        if(i+v >= 0 and i+v < row and p-v >= 0 and p-v < col):
            if(y[i+v][p-v] < 0): sv = -1
            G.add_edge(point, z[i+v][p-v]*-1*sv)
        sv = 1
        if(i-v >= 0 and i-v < row and p+v >= 0 and p+v < col):
            if(y[i-v][p+v] < 0): sv = -1
            G.add_edge(point, z[i-v][p+v]*-1*sv)

nx.draw(G, with_labels=True, pos=nx.random_layout(G)) # draws graph

# checks to make sure a path does exists from 1 to row*col
if(nx.has_path(G, source=1, target=row*col)):

    # prints path and edge order using NetworkX's dijkstra search function
    n = list(nx.dijkstra_path(G, source=1, target=row*col))
    print("\n" + "Dijkstra SearchPath: " + str(finalAnswer(n, "")))
    print("Dijkstra Search Edges: " + str(n) + "\n")

    # prints path and edge order using NetworkX's breadth first search function
    n = list(nx.bfs_edges(G, source=1))
    n = makePath(n, 1, row*col)
    print("Breadth First Search Path: " + str(finalAnswer(n, "")))
    print("Breadth First Search Edges: " + str(n) + "\n")

    #prints path and edge order using NetworkX's depth first search function
    n = list(nx.dfs_edges(G, source=1))
    n = makePath(n, 1, row*col)
    print("Depth First Search Path: " + str(finalAnswer(n, "")))
    print("Depth First Search Edges: " + str(n) + "\n")

else:
    print("No Possible Path From 1-" + str(row*col))

plt.show()
