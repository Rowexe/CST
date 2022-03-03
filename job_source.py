import threading
import time
import colorama
import webbrowser

BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

total_time = float(0)
cals = int(0)

def colour_print(text: str, effect: str) -> None:
    """
    Print `text` using the ANSI sequences to change colour, etc

    :param text: The text to print.
    :param effect: The effect we want.  One of the constants
        defined at the start of this module.
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)

def _colour(text: str, effect: str):
    colorama.init()
    colour_print(text, effect)
    colorama.deinit()

_colour("This project is made by Rowexe, github page: https://www.github.com/Rowexe", BOLD)
redirection = input("Do you want to be redirected?(y/n): ")

if redirection.lower() == "y":
    webbrowser.open_new_tab("https://www.github.com/Rowexe")
else:
    pass

parameters = 0
number1 = 2
number2 = 2
number3 = 2
number4 = 2
number5 = 2
number6 = 2
number7 = 2
number8 = 2
number9 = 2
number10 = 2

sums1 = 0
sums2 = 0
sums3 = 0
sums4 = 0
sums5 = 0
sums6 = 0
sums7 = 0
sums8 = 0
sums9 = 0
sums10 = 0

threads=10

def multiply(times):
    global number1
    global sums1

    for i in range(0,times):
        number1 *= 10000
        sums1 += 1

def multiply2(times):
    global number2
    global sums2
    for i in range(0,times):
        number2 *= 10000
        sums2 += 1

def multiply3(times):
    global number3
    global sums3

    for i in range(0,times):
        number3 *= 10000
        sums3 += 1

def multiply4(times):
    global number4
    global sums4
    for i in range(0,times):
        number4 *= 10000
        sums4 += 1

# 1-4

def oct():...

def printer(times):...

while True:
    x = input("Please enter a integer number, e to exit: ")
    if x.lower() == "e":
        quit()
    try:
        x = int(x)
        parameters = x
        half = parameters/5
        half = int(half)

        number1 = 0
        number2 = 0
        number3 = 0
        number4 = 0
        number5 = 0
        number6 = 0
        number7 = 0
        number8 = 0
        number9 = 0
        number10 = 0
        a = time.time()
        # threads

        b = time.time()

        print()
        print("\rSummary: ")
        print("{} performance threads ({} threads, {} sub threads) completed {} jobs in total with the time of {}".format(x,int(x/2),int(x/2), (sums1+sums2+sums3+sums4),b-a))
        print()
    except Exception:
        print("Please enter a integer only!")
