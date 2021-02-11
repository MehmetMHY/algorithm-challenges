![bogomeme](https://user-images.githubusercontent.com/15916367/77278015-d5b2c580-6c83-11ea-9570-7d55898f5a29.png)

# About:
Just a fun/meme Python3 project I did about Bogo Sort.

# Previous Work:
- I originally made this project back in 2019 as one of my earlier GitHub repos. It was one script and it was made as a joke. During this time, I was new to git and GitHub as a whole. Knowing this, one day I accidentally deleted that repo with my original implementation of BogoSort. Luckly, someone Forked this repo and I was able to Fork it back to my profile. 
- You can see my original implementation of BogoSort from 2019 with the following link: https://github.com/MehmetMHY/bogo-sort-meme

# BoGo Sort Module
I created a basic module for bogo sort in bs.py. This Python script has two functions:
- bogosort(list, boolean, boolean):
    - bogosort(list, False, False) = only return sorted list
    - bogosort(list, True, True) = return sorted list, # of tries, runtime, and every randomized attempt.
    - bogosort(list, True, False) = return sorted list, # of tries, and runtime.
- bogoExample(int):
	- Generates shuffled list of 0-n:
```
    bogoExample(n)
```
- Please view example.py to see an example of how to use this bs.py.
- Simple Example Script:

```
    import bs
    x = [1, 4, 5, 7, 2]
    print(bs.bogosort(x, True, False))
    print(bs.bogoExample(5))
```

## one_script/
- The one_script/ directory contains a file called: bogoSortMeme.py. This sciprt is a one script verison of the BoGo Sort module. This script was created before the BoGo Sort module in early 2019. The original project can be seen here: [[repo](https://github.com/MehmetMHY/bogo-sort-meme)]

# Bogo_Sort
BoGo Sort is one of, if not, the most ineffective sorting algorithm out there. It has a average Big O notation of O((n+1)!). Because of this, I though it would be funny to implement BoGo Sort in Python. So far, the highest list size I got sorted though Bogo Sort was 12, where a list of (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) was randomly shuffled. Sorting this list took 30 minutes and over 75 million attempts. This result is not always consistant because, due to the algorithm as a whole, it can still take longer or be faster depending on how "lucky" bogo sort gets. Its because of this that BoGo Sort is really not effective and is more of a joke rather then a proper solution for sorting.

# Why do it?
Its so bad that its a meme, so why not do it?

# Want to learn more about BoGo Sort?
Vist: [[wiki](https://en.wikipedia.org/wiki/Bogosort)]

# Requirements:
1) Python 3
2) A lot of patiences

