import datetime
from sys import argv

# the date format: 20140531

script, birthDay = argv
birthDate = datetime.date(int(birthDay[0:4]), int(birthDay[4:6]), int(birthDay[6:8]))
today = datetime.date.today()

print (today - birthDate).days + 1