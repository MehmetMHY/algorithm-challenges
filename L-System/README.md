# Simple 2D L-System Python Implmentation

## About:
- I always wanted to implment an L-System, so I did it.
- The main.py script generates the L-System and its where you can enter certain parameters for your L-System. Look for the parameters comment to see where you can enter these parameters.
- I also created a script that converts eps files to png.

## Notes:
- To apply different L-System rules, you have to modify the values in main.py.
- To generate the L-System, run the following command (after modifying the code if need be):

```
python3 main.py
```

- To convert an eps file to a png, you can use the eps_to_png.py python script by running a command like this:

```
python3 eps_to_png.py example.eps example.png
```

- This code is not perfect and is limited to 2D only. So in the feature I would like to implment this code for 3D L-Systems. I might need to use either Pygame or Unity, I will most liky use Unity for a 3D implmentation of this.

## Great Sources:
- 1) https://en.wikipedia.org/wiki/L-system
- 2) http://paulbourke.net/fractals/lsys/