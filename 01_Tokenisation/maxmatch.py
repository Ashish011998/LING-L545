import sys

dict = open(sys.argv[1]).read()

tokens = []
def maxMatch(line, dict):
    if line == "":
        return tokens
    
    for i in range(len(line), 0, -1):
        first = line[:i]
        rem = line[i:]
        if first in dict:
            sys.stdout.write(first + '\n')
            return maxMatch(rem, dict)
line = sys.stdin.readline()

while line != '':
    maxMatch(line, dict)
    line = sys.stdin.readline()