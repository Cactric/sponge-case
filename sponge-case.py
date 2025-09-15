#!/usr/bin/python3
import sys
import random
import argparse

parser = argparse.ArgumentParser("Randomly capitalise standard input and output the result on standard output")
parser.add_argument("-d","--disableansicheck", action="store_true", help="If enabled, don't check for ANSI escape characters (causes strange output from input containing things such as colours or bold text)")
parser.add_argument("-f","--frequency", type=int, default=0, help="Show a capital letter every n characters")
parser.add_argument("--onlyletters", "-o", action="store_true", help="For use with --frequency, have a capital letter every n letters (non-letter characters won't affect it)")
parser.add_argument("filenames", type=str, nargs="+", help="The files you want to read")

args = parser.parse_args()

for filename in args.filenames:
    inputfile = open(filename, 'r') if filename != "-" else sys.stdin
    
    ansi = False
    loopno = 0
    for chara in inputfile.read():
        if chara == "\033" and (not args.disableansicheck) == True:#If it's an ANSI escape code and the option is enabled...
            ansi = True#Mark it as such
        if ansi == True:
            if chara.isalpha():
                ansi = False#Stop thinking we're in an escape code once we see a letter
                #I don't think that's the standard, but it works with Neofetch now, so ¯\_(ツ)_/¯
            print(chara,end="")#If we're in an ANSI escape code, don't mess with it
        else:
            if args.frequency == 0:
                rng = random.randint(0,1)
            else:
                rng = loopno % int(args.frequency)
                #Ok, so maybe the variable being called rng is a bit confusing now        
            
            if rng == 0:
                print(chara.lower(),end="")
            else:
                print(chara.upper(),end="")
        if args.onlyletters:
            if chara.isalpha():
                loopno += 1#If --onlyletters or -o is supplied, only increment the counter if the character's a letter
        else:
            loopno += 1
