#ifndef _HANGMAN_H
#define _HANGMAN_H
#include <fstream>
#include <vector>
#include <string>
#include <map>

using namespace std;

class hangman {

public:
    void running_total();
    void print_guesses();
    void main_game();
    void guess_num();
    void word_len();
    void clearall();
    void set_map();
    void looping();
    void read();
    hangman();

private:
    bool show_cheat = false;
    bool keep_guess = false;
    string current_blanked;
    vector<string> words;
    vector<char> guess;
    char current_guess;
    int word_size;
    int guesses_num;
};

#endif
