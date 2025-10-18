// All the code below was provided for this assignment.

#include <iostream>
#include <fstream>
#include <string>
#include "maze_solver.h"

using namespace std;

bool file_exists(string filename) {
    ifstream test(filename);
    if (test) {
        test.close();
        return true;
    }
    return false;
}

int main(int argc, char* argv[]) {
	string infile;
	string s_or_q;
	bool do_pause = true;
	bool use_stack = true;

	if (argc >= 3) {
		infile = argv[1];
		s_or_q = argv[2];
		if (s_or_q != "Q" && s_or_q != "S") {
		    cerr << "Unrecognized argument: please specify stack (S) or queue (Q).  Exiting." << endl;
		}
		if (argc == 4 && string(argv[3]) == "false") do_pause = false;
		if (!file_exists(infile)) {
		    cerr << "Error opening file \"" << infile << "\" for reading, exiting." << endl;
		    return -1;
		}
	}
	else {
		cout << "Please enter a maze filename: ";
		getline(cin, infile);
		while (!file_exists(infile)) {
		    cout << "Error opening file \"" << infile << "\" for reading." << endl;
            cout << "Please enter a maze filename: ";
            getline(cin, infile);
        }
		cout << "Please enter (S) to use a stack, or (Q) to use a queue: ";
		getline(cin, s_or_q);
		while (s_or_q != "Q" && s_or_q != "S") {
            cout << "Input error: please specify stack (S) or queue (Q): ";
            getline(cin, s_or_q);
		}
	}

	use_stack = (s_or_q == "S");

	// create the maze_solver object and run it with the user inputs
	maze_solver solver(infile, use_stack, do_pause);
	solver.run();

	return 0;
}