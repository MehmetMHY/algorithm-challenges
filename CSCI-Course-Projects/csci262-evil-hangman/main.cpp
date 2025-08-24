// CSCI 262 Project 3 Evil Hangman Code
// Spring 2019

#include <iostream>
#include <string>
#include <cstdlib>
#include <cctype>
#include "hangman.h"

using namespace std;

//Used to print some text art
void print(){
    cout << endl << "=============================" << endl;
    cout << "   Welcome to Evil Hangman!  " << endl;
    cout << "=============================" << endl;
    cout << "    ___________\n"
            "    |         |\n"
            "    |         0\n"
            "    |        /|\\\n"
            "    |        / \\\n"
            "    |\n"
            "    |"<< endl;
    cout << "=============================" << endl;
    cout << " Mehmet Yilmaz | Spring 2019" << endl;
    cout << "=============================" << endl << endl;
}

//Main fuction for the code
int main() {
    while(true){
        bool leave = false;
        print();
        hangman game;
        game.word_len(); //Input validation and setter for the user's desired word length for the game.
        game.guess_num(); //Input validation and setter for the number of desired guesses by user.
        game.running_total(); //Allows the user to pick weather they want to see how many words are left during a game.
        game.read(); //Reads and stores the words from dictionary.txt into words vectors based on words' length.
        game.looping(); //Runs the guess input validation as well as main Evil-HangMan algorithm.

        while(true){ //The code here is mainly desired to allow the user to play the game again or not.
            game.clearall(); //Reset all the variables in the code.
            cout << "Whould you like to play/try again (yes or no): " << endl;
            string again;
            cin >> again;
            transform(again.begin(), again.end(), again.begin(), ::tolower);
            if(again == "no" || again == "n"){
                leave = true;
                break;
            }
            else if(again == "yes" || again == "y"){
                break;
            }else{
                cout << "Invalid Entry, Try Again!" << endl << endl;
            }
        }
        if(leave){
            cout << endl << "Thanks for Playing! " << endl;
            break;
        }
    }
    return 0;
}