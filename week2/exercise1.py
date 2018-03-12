"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

#I think this line will print a list.
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #It printed  a list of the words in the brackets.

#I think this will print a word in the list of some_words.
for word in some_words:
    print(word) #Every time I hit F5 it printed a word in the list until it ran out of words.

#I think it perform the smae funtion as before.
for x in some_words:
    print(x) #It performed the exact same function as the previous line.

#I think this is going to print the list in its brackets
print(some_words) #It printed the list in its brackets. eg. ['What', 'Does', etc]

#I think that if there are more than 3 list items in some_words than this will print out some_words contain more than 3 words.
if len(some_words) > 3:
    print('some_words contains more than 3 words') #It did exactly as I predicted.

# After reading what uname does I suspect the it might return my system specs.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    platform.uname
    
    print(platform.uname())

usefulFunction() #It returned a syntax error

#I fixed the syntax error so that the test.py would run. It now outputs my system specs.