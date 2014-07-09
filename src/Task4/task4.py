from sys import argv

# judge if the user give 2(not include the script) parameter
if len(argv) == 3:
    script, file_path, str_find = argv
else:
    # if the parameter is not correct, then exit
    print "your input is incorrect, please check it."
    exit()

# the index of which line is reading
lineCount = 0
# the count of last result
resultCount = 0

try:
    file_data = open(file_path)
    for line in file_data:
        lineCount += 1
        index = line.find(str_find)
        # if index!=-1, that indicate we find the string we want
        if index != -1:
            resultCount += 1
            print "in line:" + str(lineCount) + "," + str(index + 1)

    print "the total count is :" + str(resultCount)
# here we handle the err if the file do not exit or other err can't read the file correctly
except IOError as err:
    print "File error:" + str(err)
finally:
    if 'file_data' in locals():
        file_data.close()