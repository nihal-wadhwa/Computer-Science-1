"""
jertle.py
Author: Nihal Wadhwa
This program's purpose is to interpret an input series of symbols as a language and to execute them as various actions made in the turtle module.
"""

# Notice that this program runs as is.
# It does not do anything, but that's OK.
# As you add functionality, add test functions that you call
#   instead of the main function.
# Then run main when you are ready to try some things in normal operation.
# (Remove this block of comments before submission.)

import sys
import time
import turtle as tt

# Turtle Canvas Window Setup ######
#
WORLD_SIZE = 300  #
MARGIN = 10  #
WINDOW_SIZE = WORLD_SIZE + MARGIN  #
#
###################################

SLEEP_TIME = 5

# The Set of Jertle Commands #####################################
#
PENDOWN_CMD = "!1"  # No parameters                              #
PENUP_CMD = "!0"  # No parameters                              #
TURN_CMD = "o^"  # Parameter: angle, to the left, in degrees  #
FORWARD_CMD = "->"  # Parameter: number of units to move         #
CIRCLE_CMD = "()"  # Parameter: radius of circle                #
#
##################################################################

### PRE-DEFINED ERROR CODES ###################################
#
ILLEGAL_COMMAND = 1  # Unrecognized command string            #
MISSING_ARGUMENT = 2  # More arguments needed for this command #
NO_ARG_END = 3  # Can't find the matching closing brace  #


#
###############################################################

def error(msg, e_code):
    """
    A fatal error has occurred.
    Print an error message and end the program.
    :param msg: the string message to print before ending the program
    :param e_code: the integer error code with which the program exits
    """
    print(msg, file=sys.stderr)
    sys.exit(e_code)


def initialize():
    """
    Set up the turtle world.
    :return: None
    """
    tt.setup(WINDOW_SIZE, WINDOW_SIZE)
    tt.setworldcoordinates(-MARGIN, -MARGIN, WORLD_SIZE, WORLD_SIZE)


def locate_end_of_arg(string):
    """
    Returns the index of the next '}' in string
    Precondition: string is a string
    Postcondition: returns integer index
    """
    index = 0
    for ch in string:
        if ch == '}':
            return index
        else:
            index += 1


def interpret(program):
    """
    Takes an input program and interprets them into a set of commands that make the turtle execute various functions
    Precondition: turtle is down
    Precondition: program is a string
    Postcondition: Turtle draws commands or returns error
    """
    while program != "":
        item = program[0:2]
        program = program[2:]
        if (item != PENDOWN_CMD) and (item != PENUP_CMD) and \
                (item != TURN_CMD) and (item != FORWARD_CMD) and (item != CIRCLE_CMD):
            error("Illegal Command '" + item + "'", 1)
        if item == PENUP_CMD:
            tt.up()
        elif item == PENDOWN_CMD:
            tt.down()
        else:
            g = locate_end_of_arg(program)
            i = program[1:g]
            if item == CIRCLE_CMD:
                if len(program) == 0:
                    error("Missing opening brace for argument", 2)
                elif program[0] != "{":
                    error("Missing opening brace for argument", 2)
                elif g == None:
                    error("No closing brace on argument for '" + item + "'", 3)
                else:
                    tt.circle(int(i))
            elif item == TURN_CMD:
                if len(program) == 0:
                    error("Missing opening brace for argument", 2)
                elif program[0] != "{":
                    error("Missing opening brace for argument", 2)
                elif g is None:
                    error("No closing brace on argument for '" + item + "'", 3)
                else:
                    tt.left(int(i))
            elif item == FORWARD_CMD:
                if len(program) == 0:
                    error("Missing opening brace for argument", 2)
                elif program[0] != "{":
                    error("Missing opening brace for argument", 2)
                elif g is None:
                    error("No closing brace on argument for '" + item + "'", 3)
                else:
                    tt.forward(int(i))
            program = program[g + 1:]


def main():
    """
    Read Jertle program strings from a file and execute them.
    The file is provided by the user when this program runs.
    Stop when end of file is reached.
    :return: None
    """

    inp = input('Enter command: ')
    initialize()
    interpret(inp)
    time.sleep(SLEEP_TIME)
    tt.done()



if __name__ == "__main__":
    main()
