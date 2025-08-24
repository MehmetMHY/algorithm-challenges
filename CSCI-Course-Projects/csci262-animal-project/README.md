# CSCI262-Animal-Project

- Date: June 27, 2019

## Project Description:

Download this project, then open the pdf file called 'CSCI 262 Animal Description.pdf' for the description of this assignment. But basically, the assignment was to create a 20 Question for animals C++ program though a Binary Tree. So basically, people can create there own 20 questions in the animal.txt text file. Then a Binary Tree is created with the questions and answers in the animal.txt text file. After that, the user plays the 20 questions game and if the program guesses your animal right everything is good. But if the program does not guess your animal right, then the user can enter their own question and answer to the orginal animal.txt text file directory. If the user wants, they can also have the option to save the binary tree they created. The user can play this game as much as they want or exit the program. This program is all ran though the terminal concole. Please read the class's description of the assignment from the pdf file.

## Requriements:

1) Clion (mainly because thats what I used to develope and run this code)

## How to Run:

First download the code. Create a new Clion Project. Move the main.cpp, animal.txt, save.txt, and CMakeLists.txt into your new Clion Project. These text files are need to run this code, so dont skip up on them. You do not need to do any thing with the 'CSCI 262 Project 5 Animal WebPage'. If this does not work, create a new Clion Project. Drag the text files into the 'cmake-build-debug' folder and copy and past all the code in the main.cpp file into your new main.cpp file.

## Other Notes:

- The saved_games are stored in a text file called save.txt

- I also added some testing functions such as the history, count, and test_it functions: The history function shows the branches that a specified node is at. For example, if I want to know the history of the node “Is it an eagle?”, then when I run it in history, it would output: #Q Does it fly?->#Q Is it a bird?->#Q Is it a mammal?. The count function just returns the number of nodes in the binary tree. The test_it function just runs both the history and count function as well as show what lines were imported into the program from the text sheet. These three functions are part of the testing function groups that I made to help me with setting up the binary tree function for Part 1 of this assignment. Its not needed for the final code but it was really useful for coding and getting certain parts to work.

- The last feature I added was input validation for all the parts in the code were the user has to enter their input.
