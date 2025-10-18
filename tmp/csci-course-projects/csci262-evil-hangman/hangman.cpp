#include <algorithm>
#include "hangman.h"
#include <iostream>
#include <iterator>
#include <random>
#include <map>

using namespace std;
//The functions that do not have a commit are most likly already explained in main.cpp...
hangman::hangman() {
}

void hangman::read(){
    hangman::words;
    hangman::word_size;
    string ans;
    ifstream inFile;
    inFile.open("dictionary.txt");
    while(!inFile.eof()){
        while(std::getline(inFile,ans)){
            if(ans.length() == word_size){
                words.push_back(ans);
            }
        }
    }
}

void hangman::word_len() {
    hangman::word_size;
    while(true){
        int len = -1;
        cout << "Please enter desired Word Length: " << endl;
        cin >> len;
        if(cin.good() && len > 0 && len <= 29){
            word_size = len;
            break;
        }
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(),'\n');
        cout << "Invalid Entry, Try Again!" << endl << endl;
    }
    cout << endl;
}

void hangman::guess_num() {
    hangman::guesses_num;
    while(true){
        int len = -1;
        cout << "How many guesses do you want? " << endl;
        cin >> len;
        if(cin.good() && len > 0){
            guesses_num = len;
            break;
        }
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(),'\n');
        cout << "Invalid Entry, Try Again!" << endl << endl;
    }
    cout << endl;
}

void hangman::running_total() {
    hangman::show_cheat;
    while(true){
        string ans;
        cout << "Do you want a running total of the # of words remaining in the word list (yes or no)? " << endl;
        cin >> ans;
        transform(ans.begin(), ans.end(), ans.begin(), ::tolower);
        if(ans == "yes" || ans == "y"){
            show_cheat = true;
            break;
        }else if(ans == "no" || ans == "n"){
            break;
        }
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(),'\n');
        cout << "Invalid Entry, only yes or no are valid inputs. Try Again!" << endl << endl;
    }
}

//Displays what words have already been guesses by the user:
void hangman::print_guesses() {
    hangman::guess;
    for(int i = 0; i < guess.size(); i++){
        cout << guess[i] << " | ";
    }
    cout << endl;
}

//Main Evil HangMan algorithm though vectors and maps:
void hangman::set_map() {
    map<int, vector<string>> largest_family;
    map<int, string> current_blank;
    hangman::words;
    hangman::current_blanked;
    hangman::keep_guess;
    vector<string> family = words;

    for(int i = 0; i < family.size(); i++){
        string add;
        for(int p = 0; p < family[i].length(); p++){
            if(family[i][p] != current_guess){
                family[i][p] = '-';
            }
        }
    }

    vector<string> family_shortened = family;
    sort(family_shortened.begin(), family_shortened.end());
    family_shortened.erase( unique( family_shortened.begin(), family_shortened.end() ), family_shortened.end() );

    for(int i = 0; i < family_shortened.size(); i++){
        string check = family_shortened[i];
        vector<string> one;
        for(int p = 0; p < family.size(); p++){
            if(check == family[p]){
                one.push_back(words[p]);
            }
        }
        largest_family.insert(pair<int,vector<string>>(one.size(), one));
        current_blank.insert(pair<int,string>(one.size(), check));
    }

    string cb2 = current_blank.rbegin()->second;
    words = largest_family.rbegin()->second;
    if(current_blanked.empty()){
        current_blanked = cb2;
    }else{
        for(int i = 0; i < current_blanked.length(); i++){
            if(cb2[i] != '-'){
                current_blanked[i] = cb2[i];
                keep_guess = true;
            }
        }
    }
}

//Part of the code that allows the user to guess a letter and use the Evil HangMan alorithm:
void hangman::main_game() {
    hangman::guess;
    hangman::guesses_num;
    hangman::words;
    hangman::current_guess;
    hangman::current_blanked;
    hangman::keep_guess;

    cout << endl;
    cout << "Guesses Remaining: " << guesses_num << endl;
    cout << "Previous Guesses: ";
    print_guesses();
    cout << "Current Blanked-Out: " << current_blanked << endl;

    if(show_cheat){
        cout << "# of Words Left: " << words.size() << endl;
    }

    cout << endl;
    vector<char> letters = {'a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z','n'};
    while(true){
        string g;
        bool exit = false;
        cout << "Please guess a single letter guess: " << endl;
        cin >> g;
        transform(g.begin(), g.end(), g.begin(), ::tolower);
        for(int i = 0; i < letters.size(); i++){
            if(g.length() == 1 && g[0] == letters[i]){
                exit = true;
                char g2 = g[0];
                guess.push_back(g2);
                current_guess = g2;
                break;
            }
        }
        if(exit){
            break;
        }
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(),'\n');
        cout << "Invalid Entry, only a char. Try Again!" << endl << endl;
    }

    set_map();
    if(keep_guess){
        guesses_num++;
        keep_guess = false;
    }
    guesses_num--;
}

//Fuction that loops though the set_map() and main_game() function until the number of guesses = 0:
void hangman::looping() {
    hangman::guesses_num;
    hangman::current_blanked;
    hangman::words;
    hangman::word_size;

    cout << endl;
    while(true){
        if(words.size() == 0){
            cout << "Sorry no word has a size/length of " << word_size << ", please enter something else. " << endl << endl;
            break;
        }else{
            main_game();
            bool win = true;
            for(int i = 0; i < current_blanked.length(); i++){
                if(current_blanked[i] == '-'){
                    win = false;
                    break;
                }
            }
            if(guesses_num == 0){
                cout << endl << "=============================" << endl;
                cout << "    ___________\n"
                        "    |         |\n"
                        "    |         x\n"
                        "    |        /|\\\n"
                        "    |        / \\\n"
                        "    |\n"
                        "    |"<< endl;
                cout << "=============================" << endl;
                cout << "Out of Tries, Game Ended" << endl;
                int r = (int)(rand()%words.size());
                cout << "Correct Answer: " << words[r] << endl << endl;
                break;
            }else if(win){
                cout << endl << "=============================" << endl;
                cout << "    ___________" << endl;
                cout << "    |         |" << endl;
                cout << "    |         o" << endl;
                cout << "    |      " << endl;
                cout << "    |         \\0/ " << endl;
                cout << "    |          |" << endl;
                cout << "    |         / \\" << endl;
                cout << "=============================" << endl;
                cout << "Congrates you won! " << endl;
                cout << "Word: " << current_blanked << endl << endl;
                break;
            }
        }
    }
}

void hangman::clearall() {
    hangman::show_cheat;
    hangman::current_blanked;
    hangman::words;
    hangman::guess;
    hangman:current_guess;
    hangman::word_size;
    hangman::guesses_num;
    hangman::keep_guess;
    char reset;
    show_cheat = false;
    keep_guess = false;
    current_blanked.clear();
    words.clear();
    guess.clear();
    current_guess = reset;
    word_size = 0;
    guesses_num = 0;
}