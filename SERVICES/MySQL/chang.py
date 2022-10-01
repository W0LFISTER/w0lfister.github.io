#!/usr/bin/python

import sys
import fileinput

filepath = './test.txt'
##Function to add code block
def codeblock():
    x = '```bash\n' + line[1:]
    y = x[:-2] + '\n```' 
    f.write(y)

f= open('./output.txt', 'a')
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        if line != '\n':
            if line[0] == '`':
                codeblock()
                #print(line)
                line = fp.readline()
                cnt += 1
            else:
                f.write(line)
                line = fp.readline()
                cnt += 1
        else:
            line = fp.readline()
            cnt += 1
# replace all occurrences of 'sit' with 'SIT' and insert a line after the 5th
#for i, line in enumerate(fileinput.input('./test.txt', inplace=1)):
#    print ("x")
#     sys.stdout.write(line.replace('sit', 'SIT'))  # replace 'sit' and write
