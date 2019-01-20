import pandas as pd
import numpy as np
import Section as Sec
import os
from datetime import date
from datetime import datetime
from datetime import timedelta
import datetime

sectionscompleted = int(input('Number of sections completed to date: '))
mostrecentmodulescompleted = int(input('Number of modules finished in most recent unfinished section: '))


sectionnames = []
modulesections = {}
modulesims = {}
totallist = []
#                  1, 2, 3, 4, 5, 6, 7, 8, 9, 10
numberofmodules = [8, 9, 8, 8, 6, 6, 7, 6, 6, 7]
numberofsims    = [2, 1, 3, 2, 2, 3, 3, 3, 1, 1]

for i in range(10):
    sectionnames.append('F' + str(i + 1))

m = 0
s = 0
for section in sectionnames:
    modules = []
    for i in range(numberofmodules[m]):
        modules.append('M' + str(i + 1))
    modulesections[section] = modules
    sims = []
    for i in range(numberofsims[s]):
        sims.append(('S' + str(i + 1)))
    modulesims[section] = sims
    m += 1
    s += 1
'''
for section in sectionnames:
    sectionobject = Sec.Section(section, modulesections[section], modulesims[section], False, 0)
    totallist.append(sectionobject)

for object in totallist:
    print(object.getname() + ': ', 'Modules:', len(object.getmodules()), 'Sims:', len(object.getsims()))
'''

duedate = date(2019, 2, 4)
currentdate = date.today()
print()
print("Today's date            :", str(currentdate))
print('Practice exam start date:', str(duedate))
print()
days = (duedate - currentdate).days
print('\nTotal number of days until practice exam start date:',days)

totaltasks = 0
counter = sectionscompleted
while counter < len(numberofmodules):
    totaltasks = totaltasks + numberofmodules[counter]
    totaltasks = totaltasks + numberofsims[counter]
    counter += 1

totaltasks = totaltasks - mostrecentmodulescompleted

print('Total Tasks to Complete:', totaltasks)
print('Total Tasks per day to complete:', round(totaltasks/days,0))
