# Title:    Project 1 - Uniformed Search
# Class:    CSCI404
# Date:     2-16-2021
# Author:   Mehmet Yilmaz

# load text file into a list of lists
def file_to_list(filename):
    with open(filename) as file:
        results = [i.strip() for i in file.readlines()]
    return results

# remove any noise from the textfile, if need be
def custom_clean(data):
    ans = []
    for tmp in data:
        if(tmp != "" and tmp != "END OF INPUT"):
            ans.append(tmp.split(" "))
    return ans

# create NetWorkX graph after textfile has been loaded into a list of list (nx3 matrix)
def create_graph(textfile):
    G = nx.DiGraph()

    for i in range(len(textfile)):
        tmp = textfile[i]
        G.add_edge(tmp[0], tmp[1], weight=int(tmp[2]))

    return G.to_undirected()

# final print function for the final output
def valid_print(G, point_one, point_two, total_distance, short_path):
    distance_print = "distance: " + str(total_distance)

    if(len(short_path) == 0):
        print(distance_print)
        print("route:")
        print("none")
    else:
        print(distance_print + " km")
        print("route:")
        if(len(short_path) == 1):
            print(str(point_one) + " to " + str(point_two) + ", 0 km")
        else:
            for i in range(len(short_path)-1):
                s = short_path[i]
                t = short_path[i+1]
                D = int(G.get_edge_data(s, t)['weight'])
                print(str(s) + " to " + str(t) + ", " + str(D) + " km")

# check function to determine if inputted source and target nodes are valid or not
def initial_checkups(G, point_one, point_two):
    p1_exists = G.has_node(point_one)
    p2_exists = G.has_node(point_two)

    # check if the nodes exist in the graph
    if(p1_exists and p2_exists):
        # check to see if a path from the source to the target exists
        if(nx.has_path(G, point_one, point_two) == False):
            valid_print(G, point_one, point_two, "infinity", [])
        else:
            return True
    # print out which of the inputted nodes in the graph does not exist
    else:
        print("The following nodes do not exist, so your input is invalid:")
        if(p1_exists == False):
            print("->", point_one)
        if(p2_exists == False):
            print("->", point_two)
    return False

# *main uniform cost search function
def uniform_cost_search(G, point_one, point_two):
    priority_queue = PriorityQueue()
    priority_queue.put((0, point_one, []))

    while not priority_queue.empty():
        top_queue = priority_queue.get()

        current_node = top_queue[1]
        traveled_distance = top_queue[0]
        visited_nodes = top_queue[2]

        if(current_node == point_two):
            visited_nodes.append(current_node)
            valid_print(G, point_one, point_two, traveled_distance, visited_nodes)
            break

        neighbor_nodes = list(G.edges(current_node))

        for node in neighbor_nodes:
            name = node[1]
            distance = int(G.get_edge_data(current_node, name)['weight']) + traveled_distance
            visited_tmp = visited_nodes.copy()
            visited_tmp.append(current_node)
            priority_queue.put((distance, name, visited_tmp))

# determine if the inputed argments is valid
#   - is there 3 argments? [filepath, source_node, target_node]
#   - does the filepath/file exist?
def check_argment(inputs):
    if(len(inputs) == 3):
        if(os.path.isfile(inputs[0])):
            return True
    return False

# main function calls
if __name__ == "__main__":
    # make sure required python3 libraries are installed
    try:
        from queue import PriorityQueue
        import networkx as nx
        import sys
        import os

        argment = list(sys.argv)
        argment.pop(0)

        if(check_argment(argment)):
            # get filepath, source node, and target node from inputed argment
            filepath, source, target = argment

            # load textfile into a list of lists and clean that data
            loaded_textfile = file_to_list(filepath)
            textfile = custom_clean(loaded_textfile)

            # create a NetWorkX graph from the loaded textfile
            G = create_graph(textfile)

            # determine if UCS should be applied, check for errors or excepts
            attempt = initial_checkups(G, source, target)

            # apply UCS from source to target nodes
            if(attempt):
                uniform_cost_search(G, source, target)
        
        else:
            print("Invalid argments!")

    # how to install required libraries if they are not installed
    except ImportError:
        print("- ERROR, the required modules are not installed!")
        print("- Please run the following command: ")
        print("     pip3 install --upgrade networkx")
