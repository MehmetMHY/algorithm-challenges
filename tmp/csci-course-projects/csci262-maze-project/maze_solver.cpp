// All the code up to line 118 was created by me, but the names of the functions,
// were provided for this assignment.

#include "maze_solver.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

void maze_solver::_read_maze(istream& in) {
    string lines;
    while(!in.eof()){
        while(std::getline(in,lines)){
            _maze.push_back(lines);
        }
    }
    _rows = _maze.at(0).at(0) - '0';
    _columns = _maze.at(0).at(_maze.at(0).size()-1) - '0';
    _maze.erase(_maze.begin());
}

void maze_solver::_print_maze() {
    maze_solver::_maze;
    for(int i = 0; i < _maze.size(); i++){
        cout << _maze.at(i) << endl;
    }
}

void maze_solver::_initialize() {
    for(int i = 0; i < _maze.size(); i++){
    	for(int j = 0; j < _maze.at(i).size(); j++){
    		if(_maze.at(i).at(j) == 'o'){
    			row_start = i;
    			column_start = j;
    		}
    	}
    }
    s_r.push(row_start);
	s_c.push(column_start);
	q_r.push(row_start);
	q_c.push(column_start);

}

void maze_solver::_stack_run() {
	if(s_r.empty()){
		_no_more_steps = true;
		return;
	}
	int x = s_r.top();
	int y = s_c.top();
	s_r.pop();
	s_c.pop();
	if(_maze.at(x).at(y) != '*'){
		if(_maze.at(x).at(y) == '.'){
			_maze.at(x).at(y) = '@';
		}
		vector<int> values = {x,(y+1),x ,(y-1), (x-1), y, (x+1), y};
		for(int i = 0; i < values.size(); i+=2){
			if(values.at(i) >= 0 && values.at(i) < _rows && values.at(i+1) >= 0 && values.at(i+1) < _columns){
				if((_maze.at(values.at(i)).at(values.at(i+1))) == '.'){
					s_r.push(values.at(i));
					s_c.push(values.at(i+1));
				}
				else if((_maze.at(values.at(i)).at(values.at(i+1))) == '*'){
					_goal_reached = true;
					_no_more_steps = true;
					break;
				}
			}
		}
	}
}

void maze_solver::_queue_run() {
	if(q_r.empty()){
		_no_more_steps = true;
		return;
	}
	int x = q_r.front();
	int y = q_c.front();
	q_r.pop();
	q_c.pop();
	if(_maze.at(x).at(y) != '*'){
		if(_maze.at(x).at(y) == '.'){
			_maze.at(x).at(y) = '@';
		}
		vector<int> values = {x,(y+1),x ,(y-1), (x-1), y, (x+1), y};
		for(int i = 0; i < values.size(); i+=2){
			if(values.at(i) >= 0 && values.at(i) < _rows && values.at(i+1) >= 0 && values.at(i+1) < _columns){
				if((_maze.at(values.at(i)).at(values.at(i+1))) == '.'){
					q_r.push(values.at(i));
					q_c.push(values.at(i+1));
				}
				else if((_maze.at(values.at(i)).at(values.at(i+1))) == '*'){
					_goal_reached = true;
					_no_more_steps = true;
					break;
				}
			}
		}
	}
}

void maze_solver::_step() {
	if(_use_stack){
		_stack_run();
	}else{
		_queue_run();
	}
}

// All the codes in the function was created by me, Mehmet.
// All the code below this line (line 118) was given for this assignment.
/***************************************************************************
    You should not need to modify code below this point.  Touch at your own
    risk!
****************************************************************************/

maze_solver::maze_solver(string infile, bool use_stak, bool pause) {
	_use_stack = use_stak;
	_do_pause = pause;

	_no_more_steps = false;
	_goal_reached = false;

	// parse out maze name for later use in creating output file name
	int pos = infile.find(".");
	if (pos == string::npos) {
		_maze_name = infile;
	} else {
		_maze_name = infile.substr(0, pos);
	}

	// open input file and read in maze
	ifstream fin(infile);

	_read_maze(fin);

	fin.close();
}

void maze_solver::run() {
    _initialize();

	cout << "Solving maze '" << _maze_name << "'." << endl;
	cout << "Initial maze: " << endl << endl;
	_print_maze();
	cout << endl;
	_pause();

	// main loop
	while (!_no_more_steps) {
		_step();
		cout << endl;
		_print_maze();
		cout << endl;
		_pause();
	}
	// final output to user
	cout << "Finished: ";
	if (_goal_reached) {
		cout << "goal reached!" << endl;
	} else {
		cout << "no solution possible!" << endl;
	}
}

void maze_solver::_pause() {
	if (!_do_pause) return;
	string foo;
	cout << "Hit Enter to continue...";
	getline(cin, foo);
}