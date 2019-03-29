#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.dev1),
    on Tue Mar 13 14:35:10 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
from pyglet.window import key
import csv
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'moviestim'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
print(filename)
# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    #originPath=u'/Users/davidgruskin/Desktop/moviestim.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
keyState=key.KeyStateHandler()

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
# store frame rate of monitor if we can measure it
win = visual.Window((800, 600))
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
mov = visual.MovieStim3(win, 'des_me.mp4', size=(640, 480),
    flipVert=False, flipHoriz=False, loop=False, pos=(0,100))
print('orig movie size=%s' % mov.size)
print('duration=%.2fs' % mov.duration)
globalClock = core.Clock()
thisResp=None
counter=0
thisKey='5'
counterlist=[]
keylist=[]
timelist=[]
textStim = visual.TextStim(win=win,
    units='pix', height = 300,
    pos=(0, -300), text= thisKey,
    alignHoriz = 'center',
    color='White')
#textStim.setAutoDraw('True')
core.wait(0)
timer=core.Clock()
while mov.status != visual.FINISHED:
    mov.draw()
    textStim.draw(win)
    timeNow=timer.getTime()
    win.flip()
    win.winHandle.push_handlers(keyState)
    counter+=1
    counterlist.append(counter)
        # get response
    if keyState[key._1]:
        thisKey='1'
    elif keyState[key._2]:
        thisKey='2'
    elif keyState[key._3]:
        thisKey='3'
    elif keyState[key._4]:
        thisKey='4'
    elif keyState[key._5]:
        thisKey='5'  
    elif keyState[key._6]:
        thisKey='6'
    elif keyState[key._7]:
        thisKey='7'
    elif keyState[key._8]:
        thisKey='8'
    elif keyState[key._9]:
        thisKey='9'
    #elif keyState[key._0]:
        #thisKey='0'  
    timelist.append(timeNow)
    keylist.append(thisKey)
    textStim = visual.TextStim(win=win,
    units='pix', height = 100,
    pos=(0, -225), text= thisKey,
    alignHoriz = 'center',
    color='White')
    allKeys=event.getKeys(keyList=['q'])
    for thisKey in allKeys:
        if thisKey!='q':
            thisResp==thisKey  # correct
        elif thisKey in ['q', 'escape']:
            zipped=zip(counterlist,timelist,keylist)
            with open(filename+'.csv','w') as f:
                writer=csv.writer(f,delimiter=',')
                writer.writerows(zipped)
            core.quit()  # abort experiment'''
thisExp.saveAsWideText(filename+'.csv',fileCollisionMethod='overwrite')
thisExp.saveAsPickle(filename, fileCollisionMethod='overwrite')



# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
zipped=zip(counterlist,keylist,timelist)
with open(filename+'.csv','w') as f:
    writer=csv.writer(f,delimiter=',')
    writer.writerows(zipped)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
