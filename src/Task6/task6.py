from sys import argv
# if you want to create a new file
# use: python task6.py inputFileName new
# if you want to overwrite the file
# use: python task6.py inputFileName overwrite
script, fileName, mode = argv

myFile = open(fileName, 'r')
data = myFile.readlines()
myFile.close()

if mode == 'new':
    newFile = open('new' + fileName, 'w')
    for line in data:
        newFile.write(line.lstrip())
    newFile.close()
if mode == 'overwrite':
    primaryFile = open(fileName, 'w')
    for line in data:
        primaryFile.write(line.lstrip())
    primaryFile.close()