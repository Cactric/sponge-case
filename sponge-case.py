#!/usr/bin/python3
import sys
import random
Options = {"help":False,"frequency":0,"random":True,"protectansi":True}
if len(sys.argv) > 1:#If the user specified arguments, see if they're file(s), open them and use them, else use standard input
    Original = ""
    FileList = sys.argv[1:]#Remove the first argument, since that will be the command
    OptionArgument = False
    OptionToModify = ""
    for loopyfile in FileList:
        if not OptionArgument:
            if loopyfile == "--help" or loopyfile == "-h":
                Options["help"] = True
            elif loopyfile == "--disableansichecking" or loopyfile == "-d":
                Options["protectansi"] = False
            elif loopyfile == "-f" or loopyfile == "--frequency":
                OptionArgument = True
                OptionToModify = "frequency"
                Options["random"] = False
            else:
                filehandle = open(loopyfile)
                Original += filehandle.read()
                filehandle.close()
        else:
            Options[OptionToModify] = loopyfile
            OptionArgument = False
    if Options["help"] == True:
        HelpMessage = """Usage: sponge-case.py [OPTION]... [FILE]...\nOutput the file(s) to standard output with random captialisation\n\nOptions:
    --help, -h:                     Show a help message
    --disableansichecking, -d:      Have the letters in ANSI codes (used for colour in a TTY, amongst other things) be affected by random capitalisation (may cause strange output from certain inputs)
    -f, --freqency <n>:             Show a captial letter every n letters  \n\nsponge-case.py was written by \"Cactric\"\nRepository: <https://github.com/Cactric/sponge-case>"""
        print(HelpMessage)
if Original == "":#If the files were empty, most likely from arguments, then read stdin
    Original = sys.stdin.read()
ansi = False
loopno = 0
for chara in Original:
    if chara == "\033" and Options["protectansi"] == True:#If it's an ANSI escape code and the option is enabled...
        ansi = True#Mark it as such
    if ansi == True:
        if chara.isalpha():
            ansi = False#Stop thinking we're in an escape code once we see a letter
            #I don't think that's the standard, but it works with Neofetch now, so ¯\_(ツ)_/¯
        print(chara,end="")#If we're in an ANSI escape code, don't mess with it
    else:
        if Options["random"]:
            rng = random.randint(0,1)
        else:
            rng = loopno % int(Options["frequency"])
            #Ok, so maybe the variable being called rng is a bit confusing now
        
        
        if rng == 0:
            print(chara.lower(),end="")
        else:
            print(chara.upper(),end="")
    loopno += 1
exit()
