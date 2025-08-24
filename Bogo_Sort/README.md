![bogomeme](./assets/meme.png)

# About

Just a fun/meme Python3 project I did about Bogo Sort.

# Previous Work

I originally made this project back in 2019 as one of my earlier GitHub repos. It was one script and it was made as a joke. During this time, I was new to git and GitHub as a whole. Knowing this, one day I accidentally deleted that repo with my original implementation of BogoSort. Luckily, someone forked this repo and I was able to fork it back to my profile.

The `_origional/` directory contains the original code from that first repo.

# BoGo Sort Module

I created a basic module for bogo sort in `bs.py`. This Python script has two functions:

- **bogosort(list, boolean, boolean):**

  - `bogosort(list, False, False)` = only return sorted list
  - `bogosort(list, True, True)` = return sorted list, # of tries, runtime, and every randomized attempt
  - `bogosort(list, True, False)` = return sorted list, # of tries, and runtime

- **bogoExample(int):**
  - Generates shuffled list of 0-n:
  ```python
  bogoExample(n)
  ```

Please view `example.py` to see an example of how to use this `bs.py`.

**Simple Example Script:**

```python
import bs
x = [1, 4, 5, 7, 2]
print(bs.bogosort(x, True, False))
print(bs.bogoExample(5))
```

## one_script/

The `one_script/` directory contains a file called `bogoSortMeme.py`. This script is a one script version of the BoGo Sort module. This script was created before the BoGo Sort module in early 2019.

# Bogo Sort

BoGo Sort is one of, if not, the most ineffective sorting algorithm out there. It has an average Big O notation of O((n+1)!). Because of this, I thought it would be funny to implement BoGo Sort in Python. So far, the highest list size I got sorted through Bogo Sort was 12, where a list of (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) was randomly shuffled. Sorting this list took 30 minutes and over 75 million attempts. This result is not always consistent because, due to the algorithm as a whole, it can still take longer or be faster depending on how "lucky" bogo sort gets. It's because of this that BoGo Sort is really not effective and is more of a joke rather than a proper solution for sorting.

# Why do it?

It's so bad that it's a meme, so why not do it?

# Want to learn more about BoGo Sort?

Visit: [Bogosort Wikipedia](https://en.wikipedia.org/wiki/Bogosort)

# Requirements

1. Python 3
2. A lot of patience
