#!/usr/bin/python3
import sys
import random
loopno = 0
if len(sys.argv) > 1:#If the user specified a file, open it and use it, else use standard input
    filehandle = open(sys.argv[1])
    Original = filehandle.read()
    filehandle.close()
else:
    Original = sys.stdin.read()
ansi = False
for chara in Original:
    if chara == "\033":#If it's an ANSI escape code...
        ansi = True#Mark it as such
    if ansi == True:
        if chara.isalpha():
            ansi = False#Stop thinking we're in an escape code once we see a letter
            #I don't think that's the standard, but it works with Neofetch now, so ¯\_(ツ)_/¯
        print(chara,end="")#If we're in an ANSI escape code, don't mess with it
    else:
        rng = random.randint(0,1)#loopno % 2
        if rng == 0:
            print(chara.lower(),end="")
        else:
            print(chara.upper(),end="")
    loopno += 1
exit()
