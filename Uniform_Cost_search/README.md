# CSCI404 - Project 1 (Implment Uniform Cost Search Algorithm)
- Date: 2-16-2021

## Details:
- This was a project assigned to me for my CSCI404 (Artificial Intelligence) at the Colorado School of Mines.
- I implemented and completed this project during the Spring 2021 semester.
- The goal of this project was to implment the Uniform Cost Search algorithm.
- The input for this project would be a text file were each line contains what two nodes are connected to each other as well as the distance between those nodes. Please view the provided input file (input1.txt) to see in more detail how the input text file should be formated.
- All the code was implmented and tested by me (Mehmet).
- My school and this class (CSCI404) provided me this project/challenge as well as the "input1.txt" file for this project. 

## Learn More About Uniform-Cost Search:
- Here is a great source: https://www.educative.io/edpresso/what-is-uniform-cost-search

## Requirements:
- Language: Python 3.8.7
- Libraries:
	- networkx:
		- install: pip3 install networkx
		- link: https://networkx.org/documentation/stable/install.html#

## Tested On:
- macOS Catalina (Version 10.15.7)

## How to Run:
- 1) Install pre-requirements:
		- Python3: https://www.python.org/downloads/
		- NetworkX: https://networkx.org/documentation/stable/install.html
- 2) Make sure you have a graph data file. We will use "input1.txt" for this tutorial.
- 3) Run the following command:
		- command:	python3 find_route.py <text_file> <source_node> <target_node>
		- example:	python3 find_route.py input1.txt Luebeck Munich

## How The Code Works:
- All the code is in one file, find_route.py
- The code works by first by making sure NetworkX is installed. Then by doing input-validation to the arguments inputed into the script. After that another input-validation is applied to the inputed source and target nodes. An error message is printed to the console if the input-validation fails in any case. After that, the inputed values and data is checked to see if it fits into any of the edge cases. If the inputed values and data is not an edge case, the inputs are feed into the uniform cost search function which finds the shortest path using UCS. Finally, when a path and distance is determined, the results are printed out as the final output.
- The code depends on the NetworkX package, which can be installed using the information from (2).
- The code is divided into the following functions:
	- file_to_list() : Load input textfile data inot a list where each index is a list created by spliting a line from the textfile by a space.
	- custom_clean() : Remove any index in a list each equal "" or "END OF INPUT".
	- create_graph() : Given a list of lists, were each index holds edge data, a NetworkX undirected graph data structure is created and returned.
	- valid_print() : A function used to print the final output of the code.
	- initial_checkups() : A check function to return invalid output messages for cases where a path does not exist between two nodes and if the inputed nodes are in the graph.
	- uniform_cost_search() : The Uniform Cost Search function for the project.
	- check_argment() : Checks inputed argments for the script and makes sure its valid for the rest of the code.
- My code is structured to handle the following errors:
	- when the inputed file does not exist
	- when the inputed source node and/or target node does not exist
	- when a path does not exist between the source and target nodes
	- any import errors, usually caused by not having a certain python package installed
