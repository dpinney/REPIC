### Intro

REPIC is a Python function that will let you print output to comments inside the current file. It stands for Read, Evaluate, Print In Comments.

### Install

Install [Python 2.7.x](https://www.python.org/downloads/) and then in the terminal install via:

```bash
pip install REPIC
```

### Usage Example

Given a file test.py with the following content:

```python
from REPIC import REPIC
test = [1,2,3] + [4,5,6]
REPIC(test)
```

After running the contents of test.py become:

```python
from REPIC import REPIC
test = [1,2,3] + [4,5,6]
REPIC(test)#OUTPUT: [1,2,3,4,5,6]
```

### Why

Why in the world did I build this? I'm a huge fan or REPLs, but it's hard to save the output from them and go back and edit it later. iPython is great, it's probably the environment I develop Python in fastest, but with all the HTML and javascript frontend there's a lot of dependencies and new interfaces. REPIC lets you stay in your text editor or terminal environment and still get that convenient combination of code and output.

This library works great with Python 2.7 files edited with Sublime text. You run the file and the output shows up immediately. This might not be the case in every editor and Python environment since this code uses a lot of hackish features.

### Thanks

[iPython](https://ipython.org) was a big inspiration, and its [repl sessions can be saved](http://stackoverflow.com/questions/947810/how-to-save-a-python-interactive-session) if you prefer that kind of interface.

Thanks to users on stackoverflow for [info on how to pull line numbers out of currently executing code](http://stackoverflow.com/questions/3056048/filename-and-line-number-of-python-script). Thanks also to [this thread discussing in-place rewrites of files in Python](http://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python).

On a more philosophical level, this was inspired by [Don Knuth's literate programming](https://en.wikipedia.org/wiki/Literate_programming), [REPLs](https://en.wikipedia.org/wiki/Read–eval–print_loop), and what appears to be the first "Notebook" interface tweak to the REPL in [Mathematica](https://www.wolfram.com/mathematica/).
