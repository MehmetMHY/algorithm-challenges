# Simple 2D L-System Python Implmentation

## About:
- I always wanted to implment an L-System, so I did it.
- To learn more about L-Systems, please check out the wikipedia link in the sources section.
- This project consists of the following files:
	- draw.py : class with function which does all the L-System drawing using turtle.
	- pfuncs.py : class with functions used to save/load pickle files with L-System saves. It also contains functions for getting the current pwd and creating a list of every file path to a pickle file in the project folder.
	- main.py : main python script for this project. Here the GUI is setup and ran as well as everything else. The main.py script depends on draw.py and puncs.py.
- Run main.py script to run everything, with the following command:

```
python3 main.py
```
- Run the main.py script without the initial warning everytime:
```
python3 main.py -nw
```
- For this project, there are two other directories:
	- assets : contains random files and some backup files
	- saves : contains all the L-System saves I saved so far
- To convert an eps file to a png, you can use the eps_to_png.py python script by running a command like this:

```
python3 eps_to_png.py example.eps example.png
```
- This code is not perfect and is limited to 2D only. So in the feature I would like to implment this code for 3D L-Systems. I might need to use either Pygame or Unity, I will most liky use Unity for a 3D implmentation of this.

## Great Sources:
- 1) https://en.wikipedia.org/wiki/L-system
- 2) http://paulbourke.net/fractals/lsys/
- 3) http://www.motionesque.com/beautyoffractals/
- 4) http://paulbourke.net/fractals/lsys/
- 5) https://www.python-course.eu/tkinter_entry_widgets.php
