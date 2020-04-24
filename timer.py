#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from sys import stdout

DEFAULT_TIME = "00:06"
DEFAULT_BREAK= "00:05"
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2k'
G1 = ""
N = "bad"
cycles = 1

curr_time = ""

def quit_screen():
    print("""
ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ 
ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ 


    Goodbye! Try harder next time...


ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ 
ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ 
ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ ಠ╭╮ಠ 
""")

def studycomplete():
    print("""
(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)


    Good job! You've successfully completed all your studying!
    Type quit to quit


ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/
""")

def breakmessage():
    print("""
(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)


    Good job! Time for a break


ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/
""")

def studymessage():
    print("""
(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)


    Good job! Time to start studying again


ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/
""")

def good_quit_screen():
    print("""
(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)(｀◔ ω ◔´)


    You did really good today!!! I'm proud of you


ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/ヽ(´▽`)/
""")

def ascii_screen():
    print("""
(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧
(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧
(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧


Hello! Welcome to STUDYBOT.
    My commands are
        Time                    = Start the timer
        Control + C             = Stop the timer
        Set 00:00 (e.g. 00:35)  = Change the time
        Quit                    = Quit


    Why do you want to study today?


(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧
(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧
(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧

      """)
    
    print("""


     """)

def function1():
    print("""

    """)

def time(args):
    min, sec = [int(x) for x in args.split(":")]
    while min > 0 or sec > 0:
        global curr_time
        global cycles
        curr_time = f"{min}:{sec:2n}"
        print(curr_time)
        if curr_time == "0: 1":

            if cycles >= 1:
                start_break()
            if cycles == 0:
                global N
                N = "good"
        
        #stdout.write(CURSOR_UP_ONE)
        #stdout.write(ERASE_LINE)
        
        sec -= 1
        if sec < 0:
            sec = 59
            min -= 1
        sleep(1)

def start_break():
    global cycles
    cycles = cycles - 1
    breakmessage()
    time(DEFAULT_TIME)
    studymessage()
    time(DEFAULT_BREAK)

def goal1(args):
    global G1
    G1 = args

def time1(args):
    global T1
    T1 = int(args)

if __name__ == "__main__":
    print("\n"*10)
    ascii_screen()
    inp = input("Enter today's goal: ")
    goal1(inp)
    inp = input("How many cycles do you want to study for?")
    time1(inp)
    print("Ok! Type time to start!")
    while True:
        inp = input(">")
        command = inp.split(" ")[0].lower()
        if command == "quit":
            if N == "good":
                good_quit_screen()
            else :
                quit_screen()
            break
        elif command == "time":
            try:
                try:
                    time(inp.split(" ")[1])
                except IndexError:
                    time(DEFAULT_TIME)
            except KeyboardInterrupt:
                print("")
                print("o(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)o")
                print("o(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)o")
                print("o(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)o")
                print("")
                print("")
                print("         Are you sure want to quit?")
                print("         You still have " + curr_time +" left!")
                print("         AND your goal of " + G1 +" still needs to be achieved")
                print("")
                print("                 Type resume to continue")
                print("                 Type quit to stop")
                print("")
                print("")
                print("o(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)o")
                print("o(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)o")
                print("o(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)o")
                
        elif command =="resume":
            try:
                try:
                    time(inp.split(" ")[1])
                except IndexError:
                    time(curr_time)
            except KeyboardInterrupt:
                print("")
                print("o(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)o")
                print("o(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)o")
                print("o(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)o")
                print("")
                print("")
                print("         Are you sure want to quit?")
                print("         You still have " + curr_time +" left!")
                print("         AND your goal of " + G1 +" still needs to be achieved")
                print("")
                print("                 Type resume to continue")
                print("                 Type quit to stop")
                print("")
                print("")
                print("o(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)o")
                print("o(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)o")
                print("o(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)oo(╥﹏╥)o")
                
        

        elif command == "set":
            DEFAULT_TIME = inp.split(" ")[1]
        elif command == "ascii":
            ascii_screen()
        else: # command == "butt":
            ascii_screen()

