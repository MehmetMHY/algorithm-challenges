![bogomeme](https://user-images.githubusercontent.com/15916367/77278015-d5b2c580-6c83-11ea-9570-7d55898f5a29.png)

# About:
Just a fun/meme Python3 project I did about Bogo Sort.

# BoGo Sort Module
I created a basic module for bogo sort in bs.py. This Python script has two functions:
- bogosort(list, boolean, boolean):
    - bogosort(list, False, False) = only return sorted list
    - bogosort(list, True, True) = return sorted list, # of tries, runtime, and every randomized attempt.
    - bogosort(list, True, False) = return sorted list, # of tries, and runtime.
- bogoExample(int):
    - bogoExample(n) = generates shuffled list of 0-n, uses bogosort(), then prints out results. This is an example of bogo sort, nothing more.

- Example Script:
    * import bs
    * x = [1, 4, 5, 7, 2]
    * print(bs.bogosort(x, True, False))
    * print(bs.bogoExample(5))

## one_script/
- The one_script/ directory contains a file called: bogoSortMeme.py. This sciprt is a one script verison of the BoGo Sort module. This script was created before the BoGo Sort module in early 2019. The original project can be seen here: [[repo](https://github.com/MehmetMHY/bogo-sort-meme)]

# Bogo_Sort
BoGo Sort is one of, if not, the most ineffective sorting algorithm out there. It has a average Big O notation of O((n+1)!). Because of this, I though it would be funny to make this BoGo Sort Python program, were you enter the number of values you want in a list. Then, that list is randomized. Fianlly, that list is sorted by BoGo Sort. After being sorted, the number of attempts is listed. So far, the highest value I got sorted with Bogo Sort was 12, (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12). It took 30 minutes and over 75 million attempts...

# Why do it?
Its so bad that its a meme, so why not do it?

# Want to learn more about BoGo Sort?
Vist: [[wiki](https://en.wikipedia.org/wiki/Bogosort)]

# Requirements:
1) Python 3
2) A lot of patiences

