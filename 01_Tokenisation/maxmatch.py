import sys

dict = open(sys.argv[1]).read()
line = sys.stdin.readline()

#i = 0
while line != '':
    i = 0
    while i < len(line):
        maxWord = ''
        #print(i, len(line))
        for j in range(i, len(line)):
            #print(j, line)
            tempWord = line[i:j+1]
            if tempWord in dict and len(tempWord) > len(maxWord):
                maxWord = tempWord
        i = i+len(maxWord)
        sys.stdout.write(maxWord + "\n")
    line = sys.stdin.readline()


