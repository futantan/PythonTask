import re

print "enter quit to exit..."
# the target string begin with 'www.' and end with '.com' or '.edu' or '.net'
pattern = re.compile(r'^www.\S+(.com|.edu|.net)$')

while True:
    inputString = raw_input("Please input the domain name:\n")
    if inputString == "quit":
        break
    match = pattern.match(inputString)
    if match:
        print 'ok'
    else:
        print 'illegal'