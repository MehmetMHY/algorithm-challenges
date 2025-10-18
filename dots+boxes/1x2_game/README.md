# Work For A 1x2 Dots & Boxes Game

## About:
- This is the work I did towards analyzing a 1x2 dots & boxes game.

## Credits:
- I would like to give credit to dylan-eck (https://github.com/dylan-eck), for providing me with the pseudocode needed to create the recursive function which generates every possible list combination given a list of char(s). The pseudocode was ultimately modifited to work for a 1x2 dots & boxes game.

## Process:
- In this analyzies, the following process(s) are done:
	1. A 1x2 dots & boxes game is represented as a list in Python and has some set rules to help determine who, player 1 or 2, has won a sqaure or not. 
	2. With the representation, every possible game state is generated for a 1x2 game.
	3. After every game state has been generated, each state is filtered into a list of all "game over" states. A "game over" state being a state in a 1x2 game where no player can make any further moves.
	4. With all the "game over" states generated, we count how many times each player won a game as well as how many of those "game over" states are drawn games.
	5. The results from step 4 is anaylized.
	6. Steps 1-5 are done again with different initial starting states and the results are compared to previous tests.
	7. After all of that, a conclusion is drawn.

## My Conclusion:
- After doing my own testing using the processes listed above, I came up with the following conclusion for a 1x2 game assuming these are two players, player 1 & 2, and the fact that player 1 plays the first move:
	- Player 1's Strategy:
		1) If Player 1 can conquer any square, they should do it no matter what for a 1x2 game.
		2) Player 1’s most realistic best outcome is a Draw. If Player 2 plays reasonably.
		3) Player 1 should only make a move for dot-to-dots 0-2 and/or 4-6, never 3, for their first move.
		4) For their second move, Player 1 should make their next dot-to-dot move on a square with the greatest number of available dot-to-dots.
	- Player 2's Strategy:
		1) If Player 2 can conquer any square, they should do it no matter what for a 1x2 game.
		2) Player 2 has a high chance of winning a dot-to- dots game just by playing second.
		3) Player 2 should make their first move on dot-to-dot 3 as it reduces any chance of Player 1 winning.
