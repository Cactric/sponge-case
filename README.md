# sponge-case

Usage: sponge-case.py [OPTION]... [FILE]...

A python script that will take input from one or more files or standard input (if no files are specified) and output it wIth RANDoM CAPtiTALisAtioN

Options:\
    --help, -h:                     Show a help message\
    --disableansicheck, -d:      	Have the letters in ANSI escape codes (used for colours in a TTY, amongst other things) be affected by random capitalisation (may cause strange output from certain inputs)\
    -f, --freqency <n>:             Show a captial letter every n characters\
    -o, --onlyletters:              Only affect the counter for capitals with letters, not just any character (for use with -f)
