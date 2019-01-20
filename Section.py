import pandas as pd
import numpy as np

class Section:
    name = ''
    modules = []
    sims = []
    completed = False
    taskscompleted = 0

    def __init__(self, name, modules, sims, completed, taskscompleted):
        self.setname(name)
        self.setmodules(modules)
        self.setsims(sims)
        self.setcompleted(completed)
        self.settaskscompleted(taskscompleted)


    def setname(self, name):
        self.name = name

    def setmodules(self, modules):
        self.modules = modules

    def setsims(self, sims):
        self.sims = sims

    def setcompleted(self, completed):
        self.completed = completed

    def settaskscompleted(self, taskscompleted):
        self.taskscompleted = taskscompleted

    def getname(self):
        return self.name

    def getmodules(self):
        return self.modules

    def getsims(self):
        return self.sims

    def getcompleted(self):
        return self.completed

    def gettaskscompleted(self):
        return self.taskscompleted
