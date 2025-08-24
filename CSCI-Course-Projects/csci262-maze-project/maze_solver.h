#ifndef _MAZE_SOLVER_H
#define _MAZE_SOLVER_H

#include <iostream>
#include <vector>
#include <stack>
#include <queue>

// Some of these variable names were given for this assignment,
// but how they were used was determined by me and I did add some
// new variables.

using namespace std;

class maze_solver {
public:
    // constructor
	maze_solver(string infile, bool use_stak, bool pause = false);

	// public methods
	void run();
	int row_start;
	int column_start;

private:
    stack<int> s_r;
    stack<int> s_c;
    queue<int> q_r;
    queue<int> q_c;

	// private instance variables
	string _maze_name;
	bool _use_stack;
	bool _do_pause;

	int _rows, _columns;
	vector<string> _maze;

	bool _no_more_steps;
	bool _goal_reached;

	// private methods you need to write
    void _read_maze(istream& in);
    void _print_maze();
    void _initialize();
    void _step();
    void _stack_run();
	void _queue_run();

    // other private methods
    void _pause();
};

#endif