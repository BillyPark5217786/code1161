# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""

def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """

    a_list = []
    while (start < stop):
         a_list.append(start)
         start += step
    return a_list


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    return range(start, stop, step)

    #Ishaans Example
    #return list(range(start, stop, step))

def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """     
    step = 2
    a_list = []
    while (start < stop):
         a_list.append(start)
         start += step
    return a_list

    #Ishaans Example
    #return lone_ranger(start, stop, 2)


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    message = "give me a number between {low} and {high}:".format(low=low,high=high)
    while True:
        input_number = int(input(message))
        if input(low < input_number < high):
            print("That's the number I'm looking for")
        elif input(low < input_number < high):
            print("Nope, Lower")
        elif input(low < input_number < high):
            print("Nup, Higher")
        else:
            return input_number

    #Ishaans Example
    """    answered = False
    while answered is False:
        num = input("Enter a number between {} and {}: ".format(low, high))
        if int(num) > low and int(num) < high:
            answered = True
            break
        print(str(answered))
    return num
    """
   

def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    #Ishaans Example
    answered = False
    while not answered:
        answered = True
        inputVar = input(message)
        try:
            inputVar = int(inputVar)
        except Exception:
            try:
                inputVar = float(inputVar)
            except Exception:
                answered = False
    return inputVar

    #First attempt
    """question = "Give me a number and no one gets hurt!"
    no = "That's not a number! Give me a number! Give me a number or I hurt this baby. Where did the baby come from? I don't know. So give me a number!"
    while True:
        try:
            input_a_number = int(input(question))
        except ValueError:
            print(no)
            continue
        else:
            break
    for x in int():
        print(no)
    else:
        for i in int():
            return "Finally a number!"
    """
    
    #Second Attempt/ Doesn't work
    """a_number = random.randint(0, sys.maxin)
    turtle = True
    while True:
        question = int(input("Give me a number and no one gets hurt!: "))
        if question == a_number:
            print("Finally a number! {}".format(question))
        elif question != a_number:
            print("That's not a number! Give me a number! Give me a number or I hurt this baby. Where did the baby come from? I don't know. So give me a number! ")
    return "Finally a Number!"
    """

def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    range_of_popes = range(low, high)
    pope = False
    while not pope:
        guess_number = int(input("Guess a number between {low} and {high}".format(low=low,high=high)))
        print("You guessed {}:".format(guess_number))
        if guess_number == range_of_popes:
            print("That's how many popes there are".format(guess_number))
            pope = True
        elif guess_number != range_of_popes:
            print ("That's not a number")
    return "Hooray"

    #IShaans Example
    """answered = False
    while answered is False:
        num = not_number_rejector("Enter a number between {} and {}: ".format(low, high))
        if int(num) > low and int(num) < high:
            answered = True
            break
        print(str(answered))
    return num
    """

if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
