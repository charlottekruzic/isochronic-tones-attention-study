#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on mars 04, 2024, at 16:29
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'choice_RTT_demo'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\charl\\Desktop\\ter_pavlovia\\choicertt\\choiceRTT_rgb_main.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1440, 900], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[1, 1, 1], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1, 1, 1]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='ptb')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='PsychToolbox')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "présentation" ---
    main_trial_instruct = visual.TextStim(win=win, name='main_trial_instruct',
        text='Vous êtes sur le point de commencer le test !\n\nAppuyez sur espace pour afficher les instructions.',
        font='Arial',
        pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard()
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    ready_button = visual.ImageStim(
        win=win,
        name='ready_button', 
        image='images/response_ready.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "instructions_1" ---
    instr = visual.TextStim(win=win, name='instr',
        text="Dans cette expérience, vous devez cliquer sur la couleur que vous avez vue, le plus rapidement possible.\n\nAppuyez sur C pour le rouge\nAppuyez sur V pour le vert\nAppuyez sur B pour le bleu\n\nAppuyez sur la barre d'espace ou cliquez/touchez l'un des boutons pour commencer.",
        font='Arial',
        units='height', pos=(0, 0.1), height=0.035, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    startInst = keyboard.Keyboard()
    startMouse = event.Mouse(win=win)
    x, y = [None, None]
    startMouse.mouseClock = core.Clock()
    response_red = visual.ImageStim(
        win=win,
        name='response_red', 
        image='images/response_red.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    response_green = visual.ImageStim(
        win=win,
        name='response_green', 
        image='images/response_green.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    response_blue = visual.ImageStim(
        win=win,
        name='response_blue', 
        image='images/response_blue.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "description_p1" ---
    instr_2 = visual.TextStim(win=win, name='instr_2',
        text='Appuyer sur espace pour démarrer la phase 1.',
        font='Arial',
        units='height', pos=(0, 0.1), height=0.035, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    startInst_2 = keyboard.Keyboard()
    startMouse_2 = event.Mouse(win=win)
    x, y = [None, None]
    startMouse_2.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trial" ---
    rightright_tile = visual.ImageStim(
        win=win,
        name='rightright_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.375, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    right_tile = visual.ImageStim(
        win=win,
        name='right_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.125, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    left_tile = visual.ImageStim(
        win=win,
        name='left_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.125, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    leftleft_tile = visual.ImageStim(
        win=win,
        name='leftleft_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.375, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    red_button = visual.ImageStim(
        win=win,
        name='red_button', 
        image='images/response_red.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    green_button = visual.ImageStim(
        win=win,
        name='green_button', 
        image='images/response_green.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    blue_button = visual.ImageStim(
        win=win,
        name='blue_button', 
        image='images/response_blue.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    targetImage = visual.ImageStim(
        win=win,
        name='targetImage', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-8.0)
    keyResp = keyboard.Keyboard()
    mouseResp = event.Mouse(win=win)
    x, y = [None, None]
    mouseResp.mouseClock = core.Clock()
    sound_1 = sound.Sound('G:/Mon Drive/school/2-master/M1/S2/TER/Projet/son/Deep Sleep [3.0Hz Delta Waves] Binaural Beats & Rain Sounds & music.wav', secs=-1, stereo=True, hamming=True,
        name='sound_1')
    sound_1.setVolume(1.0)
    
    # --- Initialize components for Routine "description_p2" ---
    instr_3 = visual.TextStim(win=win, name='instr_3',
        text='Bravo, la phase 1 est terminée !\n\nAppuyer sur espace pour démarrer la phase 2.',
        font='Arial',
        units='height', pos=(0, 0.1), height=0.035, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    startInst_3 = keyboard.Keyboard()
    startMouse_3 = event.Mouse(win=win)
    x, y = [None, None]
    startMouse_3.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trial" ---
    rightright_tile = visual.ImageStim(
        win=win,
        name='rightright_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.375, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    right_tile = visual.ImageStim(
        win=win,
        name='right_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.125, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    left_tile = visual.ImageStim(
        win=win,
        name='left_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.125, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    leftleft_tile = visual.ImageStim(
        win=win,
        name='leftleft_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.375, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    red_button = visual.ImageStim(
        win=win,
        name='red_button', 
        image='images/response_red.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    green_button = visual.ImageStim(
        win=win,
        name='green_button', 
        image='images/response_green.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    blue_button = visual.ImageStim(
        win=win,
        name='blue_button', 
        image='images/response_blue.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    targetImage = visual.ImageStim(
        win=win,
        name='targetImage', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-8.0)
    keyResp = keyboard.Keyboard()
    mouseResp = event.Mouse(win=win)
    x, y = [None, None]
    mouseResp.mouseClock = core.Clock()
    sound_1 = sound.Sound('G:/Mon Drive/school/2-master/M1/S2/TER/Projet/son/Deep Sleep [3.0Hz Delta Waves] Binaural Beats & Rain Sounds & music.wav', secs=-1, stereo=True, hamming=True,
        name='sound_1')
    sound_1.setVolume(1.0)
    
    # --- Initialize components for Routine "description_p3" ---
    instr_4 = visual.TextStim(win=win, name='instr_4',
        text='Bravo, la phase 2 est terminée !\n\nAppuyer sur espace pour démarrer la phase 3.',
        font='Arial',
        units='height', pos=(0, 0.1), height=0.035, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    startInst_4 = keyboard.Keyboard()
    startMouse_4 = event.Mouse(win=win)
    x, y = [None, None]
    startMouse_4.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "trial" ---
    rightright_tile = visual.ImageStim(
        win=win,
        name='rightright_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.375, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    right_tile = visual.ImageStim(
        win=win,
        name='right_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(0.125, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    left_tile = visual.ImageStim(
        win=win,
        name='left_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.125, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    leftleft_tile = visual.ImageStim(
        win=win,
        name='leftleft_tile', 
        image='images/grey_square.jpg', mask=None, anchor='center',
        ori=0.0, pos=(-0.375, 0), size=(0.22, 0.22),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    red_button = visual.ImageStim(
        win=win,
        name='red_button', 
        image='images/response_red.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    green_button = visual.ImageStim(
        win=win,
        name='green_button', 
        image='images/response_green.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    blue_button = visual.ImageStim(
        win=win,
        name='blue_button', 
        image='images/response_blue.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.25), size=(0.2, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    targetImage = visual.ImageStim(
        win=win,
        name='targetImage', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-8.0)
    keyResp = keyboard.Keyboard()
    mouseResp = event.Mouse(win=win)
    x, y = [None, None]
    mouseResp.mouseClock = core.Clock()
    sound_1 = sound.Sound('G:/Mon Drive/school/2-master/M1/S2/TER/Projet/son/Deep Sleep [3.0Hz Delta Waves] Binaural Beats & Rain Sounds & music.wav', secs=-1, stereo=True, hamming=True,
        name='sound_1')
    sound_1.setVolume(1.0)
    
    # --- Initialize components for Routine "end_message" ---
    end_text = visual.TextStim(win=win, name='end_text',
        text="L'expérience est terminée !\n\nMerci pour votre temps !",
        font='Arial',
        pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "présentation" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('présentation.started', globalClock.getTime())
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # setup some python lists for storing info about the mouse
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    présentationComponents = [main_trial_instruct, key_resp, mouse, ready_button]
    for thisComponent in présentationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "présentation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *main_trial_instruct* updates
        
        # if main_trial_instruct is starting this frame...
        if main_trial_instruct.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            main_trial_instruct.frameNStart = frameN  # exact frame index
            main_trial_instruct.tStart = t  # local t and not account for scr refresh
            main_trial_instruct.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_trial_instruct, 'tStartRefresh')  # time at next scr refresh
            # update status
            main_trial_instruct.status = STARTED
            main_trial_instruct.setAutoDraw(True)
        
        # if main_trial_instruct is active this frame...
        if main_trial_instruct.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # end routine on response        
        # *ready_button* updates
        
        # if ready_button is starting this frame...
        if ready_button.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            ready_button.frameNStart = frameN  # exact frame index
            ready_button.tStart = t  # local t and not account for scr refresh
            ready_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ready_button, 'tStartRefresh')  # time at next scr refresh
            # update status
            ready_button.status = STARTED
            ready_button.setAutoDraw(True)
        
        # if ready_button is active this frame...
        if ready_button.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in présentationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "présentation" ---
    for thisComponent in présentationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('présentation.stopped', globalClock.getTime())
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # store data for thisExp (ExperimentHandler)
    x, y = mouse.getPos()
    buttons = mouse.getPressed()
    thisExp.addData('mouse.x', x)
    thisExp.addData('mouse.y', y)
    thisExp.addData('mouse.leftButton', buttons[0])
    thisExp.addData('mouse.midButton', buttons[1])
    thisExp.addData('mouse.rightButton', buttons[2])
    thisExp.nextEntry()
    # the Routine "présentation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions_1.started', globalClock.getTime())
    startInst.keys = []
    startInst.rt = []
    _startInst_allKeys = []
    # setup some python lists for storing info about the startMouse
    gotValidClick = False  # until a click is received
    startMouse.mouseClock.reset()
    # keep track of which components have finished
    instructions_1Components = [instr, startInst, startMouse, response_red, response_green, response_blue]
    for thisComponent in instructions_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions_1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr* updates
        
        # if instr is starting this frame...
        if instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr.frameNStart = frameN  # exact frame index
            instr.tStart = t  # local t and not account for scr refresh
            instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr.status = STARTED
            instr.setAutoDraw(True)
        
        # if instr is active this frame...
        if instr.status == STARTED:
            # update params
            pass
        
        # *startInst* updates
        waitOnFlip = False
        
        # if startInst is starting this frame...
        if startInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startInst.frameNStart = frameN  # exact frame index
            startInst.tStart = t  # local t and not account for scr refresh
            startInst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startInst, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'startInst.started')
            # update status
            startInst.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(startInst.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(startInst.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if startInst.status == STARTED and not waitOnFlip:
            theseKeys = startInst.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
            _startInst_allKeys.extend(theseKeys)
            if len(_startInst_allKeys):
                startInst.keys = _startInst_allKeys[-1].name  # just the last key pressed
                startInst.rt = _startInst_allKeys[-1].rt
                startInst.duration = _startInst_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *startMouse* updates
        
        # if startMouse is starting this frame...
        if startMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startMouse.frameNStart = frameN  # exact frame index
            startMouse.tStart = t  # local t and not account for scr refresh
            startMouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startMouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('startMouse.started', t)
            # update status
            startMouse.status = STARTED
            prevButtonState = startMouse.getPressed()  # if button is down already this ISN'T a new click
        if startMouse.status == STARTED:  # only update if started and not finished!
            buttons = startMouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # end routine on response        
        # *response_red* updates
        
        # if response_red is starting this frame...
        if response_red.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            response_red.frameNStart = frameN  # exact frame index
            response_red.tStart = t  # local t and not account for scr refresh
            response_red.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_red, 'tStartRefresh')  # time at next scr refresh
            # update status
            response_red.status = STARTED
            response_red.setAutoDraw(True)
        
        # if response_red is active this frame...
        if response_red.status == STARTED:
            # update params
            pass
        
        # *response_green* updates
        
        # if response_green is starting this frame...
        if response_green.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            response_green.frameNStart = frameN  # exact frame index
            response_green.tStart = t  # local t and not account for scr refresh
            response_green.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_green, 'tStartRefresh')  # time at next scr refresh
            # update status
            response_green.status = STARTED
            response_green.setAutoDraw(True)
        
        # if response_green is active this frame...
        if response_green.status == STARTED:
            # update params
            pass
        
        # *response_blue* updates
        
        # if response_blue is starting this frame...
        if response_blue.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            response_blue.frameNStart = frameN  # exact frame index
            response_blue.tStart = t  # local t and not account for scr refresh
            response_blue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response_blue, 'tStartRefresh')  # time at next scr refresh
            # update status
            response_blue.status = STARTED
            response_blue.setAutoDraw(True)
        
        # if response_blue is active this frame...
        if response_blue.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_1" ---
    for thisComponent in instructions_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions_1.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "instructions_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "description_p1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('description_p1.started', globalClock.getTime())
    startInst_2.keys = []
    startInst_2.rt = []
    _startInst_2_allKeys = []
    # setup some python lists for storing info about the startMouse_2
    gotValidClick = False  # until a click is received
    startMouse_2.mouseClock.reset()
    # keep track of which components have finished
    description_p1Components = [instr_2, startInst_2, startMouse_2]
    for thisComponent in description_p1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "description_p1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_2* updates
        
        # if instr_2 is starting this frame...
        if instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_2.frameNStart = frameN  # exact frame index
            instr_2.tStart = t  # local t and not account for scr refresh
            instr_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr_2.status = STARTED
            instr_2.setAutoDraw(True)
        
        # if instr_2 is active this frame...
        if instr_2.status == STARTED:
            # update params
            pass
        
        # *startInst_2* updates
        waitOnFlip = False
        
        # if startInst_2 is starting this frame...
        if startInst_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startInst_2.frameNStart = frameN  # exact frame index
            startInst_2.tStart = t  # local t and not account for scr refresh
            startInst_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startInst_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'startInst_2.started')
            # update status
            startInst_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(startInst_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(startInst_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if startInst_2.status == STARTED and not waitOnFlip:
            theseKeys = startInst_2.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
            _startInst_2_allKeys.extend(theseKeys)
            if len(_startInst_2_allKeys):
                startInst_2.keys = _startInst_2_allKeys[-1].name  # just the last key pressed
                startInst_2.rt = _startInst_2_allKeys[-1].rt
                startInst_2.duration = _startInst_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *startMouse_2* updates
        
        # if startMouse_2 is starting this frame...
        if startMouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startMouse_2.frameNStart = frameN  # exact frame index
            startMouse_2.tStart = t  # local t and not account for scr refresh
            startMouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startMouse_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('startMouse_2.started', t)
            # update status
            startMouse_2.status = STARTED
            prevButtonState = startMouse_2.getPressed()  # if button is down already this ISN'T a new click
        if startMouse_2.status == STARTED:  # only update if started and not finished!
            buttons = startMouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in description_p1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "description_p1" ---
    for thisComponent in description_p1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('description_p1.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "description_p1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    ExptLoop1 = data.TrialHandler(nReps=4.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('RTtimeConditions_main.xlsx'),
        seed=None, name='ExptLoop1')
    thisExp.addLoop(ExptLoop1)  # add the loop to the experiment
    thisExptLoop1 = ExptLoop1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExptLoop1.rgb)
    if thisExptLoop1 != None:
        for paramName in thisExptLoop1:
            globals()[paramName] = thisExptLoop1[paramName]
    
    for thisExptLoop1 in ExptLoop1:
        currentLoop = ExptLoop1
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisExptLoop1.rgb)
        if thisExptLoop1 != None:
            for paramName in thisExptLoop1:
                globals()[paramName] = thisExptLoop1[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        # Run 'Begin Routine' code from setStimuli
        positionList = [-0.375,-0.125,0.125,0.375] #list of possible X coordinates for target to appear
        shuffle(positionList) #randomise these positions
        targetX = positionList[0] #pick the first value from the list 
        
        #thisImage is the variable in the Image field of targetImage
        if thisImage == 'images/red_dot.png': #path of where to find the target image
            corrAns = 'c' #setting the key press that will be the correct answer
            corrButton = red_button #setting the button that will be the correct answer
            corrButtonName = 'red_button' #making this a string so that it can be compared later when checking for acccuracy
        elif thisImage == 'images/green_dot.png':
            corrAns = 'v'
            corrButton = green_button
            corrButtonName = 'green_button'
        elif thisImage == 'images/blue_dot.png':
            corrAns = 'b'
            corrButton = blue_button
            corrButtonName = 'blue_button'
        
        
        targetImage.setPos([targetX, 0])
        targetImage.setImage(thisImage)
        keyResp.keys = []
        keyResp.rt = []
        _keyResp_allKeys = []
        # setup some python lists for storing info about the mouseResp
        mouseResp.x = []
        mouseResp.y = []
        mouseResp.leftButton = []
        mouseResp.midButton = []
        mouseResp.rightButton = []
        mouseResp.time = []
        mouseResp.clicked_name = []
        gotValidClick = False  # until a click is received
        mouseResp.mouseClock.reset()
        sound_1.setSound('G:/Mon Drive/school/2-master/M1/S2/TER/Projet/son/Deep Sleep [3.0Hz Delta Waves] Binaural Beats & Rain Sounds & music.wav', secs=600, hamming=True)
        sound_1.setVolume(1.0, log=False)
        sound_1.seek(0)
        # keep track of which components have finished
        trialComponents = [rightright_tile, right_tile, left_tile, leftleft_tile, red_button, green_button, blue_button, targetImage, keyResp, mouseResp, sound_1]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rightright_tile* updates
            
            # if rightright_tile is starting this frame...
            if rightright_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                rightright_tile.frameNStart = frameN  # exact frame index
                rightright_tile.tStart = t  # local t and not account for scr refresh
                rightright_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightright_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                rightright_tile.status = STARTED
                rightright_tile.setAutoDraw(True)
            
            # if rightright_tile is active this frame...
            if rightright_tile.status == STARTED:
                # update params
                pass
            
            # *right_tile* updates
            
            # if right_tile is starting this frame...
            if right_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                right_tile.frameNStart = frameN  # exact frame index
                right_tile.tStart = t  # local t and not account for scr refresh
                right_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                right_tile.status = STARTED
                right_tile.setAutoDraw(True)
            
            # if right_tile is active this frame...
            if right_tile.status == STARTED:
                # update params
                pass
            
            # *left_tile* updates
            
            # if left_tile is starting this frame...
            if left_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                left_tile.frameNStart = frameN  # exact frame index
                left_tile.tStart = t  # local t and not account for scr refresh
                left_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                left_tile.status = STARTED
                left_tile.setAutoDraw(True)
            
            # if left_tile is active this frame...
            if left_tile.status == STARTED:
                # update params
                pass
            
            # *leftleft_tile* updates
            
            # if leftleft_tile is starting this frame...
            if leftleft_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                leftleft_tile.frameNStart = frameN  # exact frame index
                leftleft_tile.tStart = t  # local t and not account for scr refresh
                leftleft_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftleft_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                leftleft_tile.status = STARTED
                leftleft_tile.setAutoDraw(True)
            
            # if leftleft_tile is active this frame...
            if leftleft_tile.status == STARTED:
                # update params
                pass
            
            # *red_button* updates
            
            # if red_button is starting this frame...
            if red_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                red_button.frameNStart = frameN  # exact frame index
                red_button.tStart = t  # local t and not account for scr refresh
                red_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                red_button.status = STARTED
                red_button.setAutoDraw(True)
            
            # if red_button is active this frame...
            if red_button.status == STARTED:
                # update params
                pass
            
            # *green_button* updates
            
            # if green_button is starting this frame...
            if green_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                green_button.frameNStart = frameN  # exact frame index
                green_button.tStart = t  # local t and not account for scr refresh
                green_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                green_button.status = STARTED
                green_button.setAutoDraw(True)
            
            # if green_button is active this frame...
            if green_button.status == STARTED:
                # update params
                pass
            
            # *blue_button* updates
            
            # if blue_button is starting this frame...
            if blue_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                blue_button.frameNStart = frameN  # exact frame index
                blue_button.tStart = t  # local t and not account for scr refresh
                blue_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blue_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                blue_button.status = STARTED
                blue_button.setAutoDraw(True)
            
            # if blue_button is active this frame...
            if blue_button.status == STARTED:
                # update params
                pass
            
            # *targetImage* updates
            
            # if targetImage is starting this frame...
            if targetImage.status == NOT_STARTED and tThisFlip >= onsetTime-frameTolerance:
                # keep track of start time/frame for later
                targetImage.frameNStart = frameN  # exact frame index
                targetImage.tStart = t  # local t and not account for scr refresh
                targetImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(targetImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'targetImage.started')
                # update status
                targetImage.status = STARTED
                targetImage.setAutoDraw(True)
            
            # if targetImage is active this frame...
            if targetImage.status == STARTED:
                # update params
                pass
            
            # if targetImage is stopping this frame...
            if targetImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > targetImage.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    targetImage.tStop = t  # not accounting for scr refresh
                    targetImage.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'targetImage.stopped')
                    # update status
                    targetImage.status = FINISHED
                    targetImage.setAutoDraw(False)
            
            # *keyResp* updates
            
            # if keyResp is starting this frame...
            if keyResp.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                keyResp.frameNStart = frameN  # exact frame index
                keyResp.tStart = t  # local t and not account for scr refresh
                keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
                # update status
                keyResp.status = STARTED
                # keyboard checking is just starting
                keyResp.clock.reset()  # now t=0
                keyResp.clearEvents(eventType='keyboard')
            if keyResp.status == STARTED:
                theseKeys = keyResp.getKeys(keyList=['b','c','v'], ignoreKeys=["escape"], waitRelease=False)
                _keyResp_allKeys.extend(theseKeys)
                if len(_keyResp_allKeys):
                    keyResp.keys = _keyResp_allKeys[-1].name  # just the last key pressed
                    keyResp.rt = _keyResp_allKeys[-1].rt
                    keyResp.duration = _keyResp_allKeys[-1].duration
                    # was this correct?
                    if (keyResp.keys == str(corrAns)) or (keyResp.keys == corrAns):
                        keyResp.corr = 1
                    else:
                        keyResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # *mouseResp* updates
            
            # if mouseResp is starting this frame...
            if mouseResp.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                mouseResp.frameNStart = frameN  # exact frame index
                mouseResp.tStart = t  # local t and not account for scr refresh
                mouseResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseResp, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouseResp.status = STARTED
                prevButtonState = mouseResp.getPressed()  # if button is down already this ISN'T a new click
            if mouseResp.status == STARTED:  # only update if started and not finished!
                buttons = mouseResp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([square_button, plus_button, cross_button], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouseResp):
                                gotValidClick = True
                                mouseResp.clicked_name.append(obj.name)
                        x, y = mouseResp.getPos()
                        mouseResp.x.append(x)
                        mouseResp.y.append(y)
                        buttons = mouseResp.getPressed()
                        mouseResp.leftButton.append(buttons[0])
                        mouseResp.midButton.append(buttons[1])
                        mouseResp.rightButton.append(buttons[2])
                        mouseResp.time.append(mouseResp.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # if sound_1 is starting this frame...
            if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.tStart = t  # local t and not account for scr refresh
                sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('sound_1.started', tThisFlipGlobal)
                # update status
                sound_1.status = STARTED
                sound_1.play(when=win)  # sync with win flip
            
            # if sound_1 is stopping this frame...
            if sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_1.tStartRefresh + 600-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_1.tStop = t  # not accounting for scr refresh
                    sound_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sound_1.stopped')
                    # update status
                    sound_1.status = FINISHED
                    sound_1.stop()
            # update sound_1 status according to whether it's playing
            if sound_1.isPlaying:
                sound_1.status = STARTED
            elif sound_1.isFinished:
                sound_1.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # check responses
        if keyResp.keys in ['', [], None]:  # No response was made
            keyResp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               keyResp.corr = 1;  # correct non-response
            else:
               keyResp.corr = 0;  # failed to respond (incorrectly)
        # store data for ExptLoop1 (TrialHandler)
        ExptLoop1.addData('keyResp.keys',keyResp.keys)
        ExptLoop1.addData('keyResp.corr', keyResp.corr)
        if keyResp.keys != None:  # we had a response
            ExptLoop1.addData('keyResp.rt', keyResp.rt)
            ExptLoop1.addData('keyResp.duration', keyResp.duration)
        # store data for ExptLoop1 (TrialHandler)
        ExptLoop1.addData('mouseResp.x', mouseResp.x)
        ExptLoop1.addData('mouseResp.y', mouseResp.y)
        ExptLoop1.addData('mouseResp.leftButton', mouseResp.leftButton)
        ExptLoop1.addData('mouseResp.midButton', mouseResp.midButton)
        ExptLoop1.addData('mouseResp.rightButton', mouseResp.rightButton)
        ExptLoop1.addData('mouseResp.time', mouseResp.time)
        ExptLoop1.addData('mouseResp.clicked_name', mouseResp.clicked_name)
        # Run 'End Routine' code from recordRTandAccuracy
        #this code is to record the reaction times and accuracy of the trial
        
        thisRoutineDuration = t # how long did this trial last
        
        # keyResp.rt is the time with which a key was pressed
        # mouseResp.time is the time with which a button was clicked/pressed
        # thisRecRT - how long it took for participants to respond after onset of targetImage
        # thisRespType - keeping track of which response component was used
        # thisAcc - whether or not the response was correct
        # correctMouseResp - name of column in data output which records the accuracy of mouse responses
        
        if keyResp.keys:
            thisRespType = 'keyboard' #record type of response 
            thisRecRT = keyResp.rt - onsetTime #record time taken to response
            if keyResp.corr == 1: #if the response is correct
                thisAcc = 'correct' #print correct
            else:
                thisAcc = 'incorrect'
        else:
            thisRespType = 'mouse'
            thisRecRT = mouseResp.time[0] - onsetTime
            if mouseResp.clicked_name[0] == corrButtonName: #check if what was clicked corresponds to the correct button
                thisAcc = 'correct'
                thisExp.addData('correctMouseResp', 1) #record accuracy of mouse clicks
            else:
                thisAcc = 'incorrect'
                thisExp.addData('correctMouseResp', 0)
        
        thisExp.addData('trialRespTimes', thisRecRT) #record the actual response times of each trial
        
        
        #print(thisRoutineDuration, thisRecRT, thisRespType, thisAcc, onsetTime)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 4.0 repeats of 'ExptLoop1'
    
    
    # --- Prepare to start Routine "description_p2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('description_p2.started', globalClock.getTime())
    startInst_3.keys = []
    startInst_3.rt = []
    _startInst_3_allKeys = []
    # setup some python lists for storing info about the startMouse_3
    gotValidClick = False  # until a click is received
    startMouse_3.mouseClock.reset()
    # keep track of which components have finished
    description_p2Components = [instr_3, startInst_3, startMouse_3]
    for thisComponent in description_p2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "description_p2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_3* updates
        
        # if instr_3 is starting this frame...
        if instr_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_3.frameNStart = frameN  # exact frame index
            instr_3.tStart = t  # local t and not account for scr refresh
            instr_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr_3.status = STARTED
            instr_3.setAutoDraw(True)
        
        # if instr_3 is active this frame...
        if instr_3.status == STARTED:
            # update params
            pass
        
        # *startInst_3* updates
        waitOnFlip = False
        
        # if startInst_3 is starting this frame...
        if startInst_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startInst_3.frameNStart = frameN  # exact frame index
            startInst_3.tStart = t  # local t and not account for scr refresh
            startInst_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startInst_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'startInst_3.started')
            # update status
            startInst_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(startInst_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(startInst_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if startInst_3.status == STARTED and not waitOnFlip:
            theseKeys = startInst_3.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
            _startInst_3_allKeys.extend(theseKeys)
            if len(_startInst_3_allKeys):
                startInst_3.keys = _startInst_3_allKeys[-1].name  # just the last key pressed
                startInst_3.rt = _startInst_3_allKeys[-1].rt
                startInst_3.duration = _startInst_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *startMouse_3* updates
        
        # if startMouse_3 is starting this frame...
        if startMouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startMouse_3.frameNStart = frameN  # exact frame index
            startMouse_3.tStart = t  # local t and not account for scr refresh
            startMouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startMouse_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('startMouse_3.started', t)
            # update status
            startMouse_3.status = STARTED
            prevButtonState = startMouse_3.getPressed()  # if button is down already this ISN'T a new click
        if startMouse_3.status == STARTED:  # only update if started and not finished!
            buttons = startMouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in description_p2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "description_p2" ---
    for thisComponent in description_p2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('description_p2.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "description_p2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    ExptLoop2 = data.TrialHandler(nReps=100.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('RTtimeConditions_main.xlsx'),
        seed=None, name='ExptLoop2')
    thisExp.addLoop(ExptLoop2)  # add the loop to the experiment
    thisExptLoop2 = ExptLoop2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExptLoop2.rgb)
    if thisExptLoop2 != None:
        for paramName in thisExptLoop2:
            globals()[paramName] = thisExptLoop2[paramName]
    
    for thisExptLoop2 in ExptLoop2:
        currentLoop = ExptLoop2
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisExptLoop2.rgb)
        if thisExptLoop2 != None:
            for paramName in thisExptLoop2:
                globals()[paramName] = thisExptLoop2[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        # Run 'Begin Routine' code from setStimuli
        positionList = [-0.375,-0.125,0.125,0.375] #list of possible X coordinates for target to appear
        shuffle(positionList) #randomise these positions
        targetX = positionList[0] #pick the first value from the list 
        
        #thisImage is the variable in the Image field of targetImage
        if thisImage == 'images/red_dot.png': #path of where to find the target image
            corrAns = 'c' #setting the key press that will be the correct answer
            corrButton = red_button #setting the button that will be the correct answer
            corrButtonName = 'red_button' #making this a string so that it can be compared later when checking for acccuracy
        elif thisImage == 'images/green_dot.png':
            corrAns = 'v'
            corrButton = green_button
            corrButtonName = 'green_button'
        elif thisImage == 'images/blue_dot.png':
            corrAns = 'b'
            corrButton = blue_button
            corrButtonName = 'blue_button'
        
        
        targetImage.setPos([targetX, 0])
        targetImage.setImage(thisImage)
        keyResp.keys = []
        keyResp.rt = []
        _keyResp_allKeys = []
        # setup some python lists for storing info about the mouseResp
        mouseResp.x = []
        mouseResp.y = []
        mouseResp.leftButton = []
        mouseResp.midButton = []
        mouseResp.rightButton = []
        mouseResp.time = []
        mouseResp.clicked_name = []
        gotValidClick = False  # until a click is received
        mouseResp.mouseClock.reset()
        sound_1.setSound('G:/Mon Drive/school/2-master/M1/S2/TER/Projet/son/Deep Sleep [3.0Hz Delta Waves] Binaural Beats & Rain Sounds & music.wav', secs=600, hamming=True)
        sound_1.setVolume(1.0, log=False)
        sound_1.seek(0)
        # keep track of which components have finished
        trialComponents = [rightright_tile, right_tile, left_tile, leftleft_tile, red_button, green_button, blue_button, targetImage, keyResp, mouseResp, sound_1]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rightright_tile* updates
            
            # if rightright_tile is starting this frame...
            if rightright_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                rightright_tile.frameNStart = frameN  # exact frame index
                rightright_tile.tStart = t  # local t and not account for scr refresh
                rightright_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightright_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                rightright_tile.status = STARTED
                rightright_tile.setAutoDraw(True)
            
            # if rightright_tile is active this frame...
            if rightright_tile.status == STARTED:
                # update params
                pass
            
            # *right_tile* updates
            
            # if right_tile is starting this frame...
            if right_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                right_tile.frameNStart = frameN  # exact frame index
                right_tile.tStart = t  # local t and not account for scr refresh
                right_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                right_tile.status = STARTED
                right_tile.setAutoDraw(True)
            
            # if right_tile is active this frame...
            if right_tile.status == STARTED:
                # update params
                pass
            
            # *left_tile* updates
            
            # if left_tile is starting this frame...
            if left_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                left_tile.frameNStart = frameN  # exact frame index
                left_tile.tStart = t  # local t and not account for scr refresh
                left_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                left_tile.status = STARTED
                left_tile.setAutoDraw(True)
            
            # if left_tile is active this frame...
            if left_tile.status == STARTED:
                # update params
                pass
            
            # *leftleft_tile* updates
            
            # if leftleft_tile is starting this frame...
            if leftleft_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                leftleft_tile.frameNStart = frameN  # exact frame index
                leftleft_tile.tStart = t  # local t and not account for scr refresh
                leftleft_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftleft_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                leftleft_tile.status = STARTED
                leftleft_tile.setAutoDraw(True)
            
            # if leftleft_tile is active this frame...
            if leftleft_tile.status == STARTED:
                # update params
                pass
            
            # *red_button* updates
            
            # if red_button is starting this frame...
            if red_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                red_button.frameNStart = frameN  # exact frame index
                red_button.tStart = t  # local t and not account for scr refresh
                red_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                red_button.status = STARTED
                red_button.setAutoDraw(True)
            
            # if red_button is active this frame...
            if red_button.status == STARTED:
                # update params
                pass
            
            # *green_button* updates
            
            # if green_button is starting this frame...
            if green_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                green_button.frameNStart = frameN  # exact frame index
                green_button.tStart = t  # local t and not account for scr refresh
                green_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                green_button.status = STARTED
                green_button.setAutoDraw(True)
            
            # if green_button is active this frame...
            if green_button.status == STARTED:
                # update params
                pass
            
            # *blue_button* updates
            
            # if blue_button is starting this frame...
            if blue_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                blue_button.frameNStart = frameN  # exact frame index
                blue_button.tStart = t  # local t and not account for scr refresh
                blue_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blue_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                blue_button.status = STARTED
                blue_button.setAutoDraw(True)
            
            # if blue_button is active this frame...
            if blue_button.status == STARTED:
                # update params
                pass
            
            # *targetImage* updates
            
            # if targetImage is starting this frame...
            if targetImage.status == NOT_STARTED and tThisFlip >= onsetTime-frameTolerance:
                # keep track of start time/frame for later
                targetImage.frameNStart = frameN  # exact frame index
                targetImage.tStart = t  # local t and not account for scr refresh
                targetImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(targetImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'targetImage.started')
                # update status
                targetImage.status = STARTED
                targetImage.setAutoDraw(True)
            
            # if targetImage is active this frame...
            if targetImage.status == STARTED:
                # update params
                pass
            
            # if targetImage is stopping this frame...
            if targetImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > targetImage.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    targetImage.tStop = t  # not accounting for scr refresh
                    targetImage.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'targetImage.stopped')
                    # update status
                    targetImage.status = FINISHED
                    targetImage.setAutoDraw(False)
            
            # *keyResp* updates
            
            # if keyResp is starting this frame...
            if keyResp.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                keyResp.frameNStart = frameN  # exact frame index
                keyResp.tStart = t  # local t and not account for scr refresh
                keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
                # update status
                keyResp.status = STARTED
                # keyboard checking is just starting
                keyResp.clock.reset()  # now t=0
                keyResp.clearEvents(eventType='keyboard')
            if keyResp.status == STARTED:
                theseKeys = keyResp.getKeys(keyList=['b','c','v'], ignoreKeys=["escape"], waitRelease=False)
                _keyResp_allKeys.extend(theseKeys)
                if len(_keyResp_allKeys):
                    keyResp.keys = _keyResp_allKeys[-1].name  # just the last key pressed
                    keyResp.rt = _keyResp_allKeys[-1].rt
                    keyResp.duration = _keyResp_allKeys[-1].duration
                    # was this correct?
                    if (keyResp.keys == str(corrAns)) or (keyResp.keys == corrAns):
                        keyResp.corr = 1
                    else:
                        keyResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # *mouseResp* updates
            
            # if mouseResp is starting this frame...
            if mouseResp.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                mouseResp.frameNStart = frameN  # exact frame index
                mouseResp.tStart = t  # local t and not account for scr refresh
                mouseResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseResp, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouseResp.status = STARTED
                prevButtonState = mouseResp.getPressed()  # if button is down already this ISN'T a new click
            if mouseResp.status == STARTED:  # only update if started and not finished!
                buttons = mouseResp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([square_button, plus_button, cross_button], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouseResp):
                                gotValidClick = True
                                mouseResp.clicked_name.append(obj.name)
                        x, y = mouseResp.getPos()
                        mouseResp.x.append(x)
                        mouseResp.y.append(y)
                        buttons = mouseResp.getPressed()
                        mouseResp.leftButton.append(buttons[0])
                        mouseResp.midButton.append(buttons[1])
                        mouseResp.rightButton.append(buttons[2])
                        mouseResp.time.append(mouseResp.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # if sound_1 is starting this frame...
            if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.tStart = t  # local t and not account for scr refresh
                sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('sound_1.started', tThisFlipGlobal)
                # update status
                sound_1.status = STARTED
                sound_1.play(when=win)  # sync with win flip
            
            # if sound_1 is stopping this frame...
            if sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_1.tStartRefresh + 600-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_1.tStop = t  # not accounting for scr refresh
                    sound_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sound_1.stopped')
                    # update status
                    sound_1.status = FINISHED
                    sound_1.stop()
            # update sound_1 status according to whether it's playing
            if sound_1.isPlaying:
                sound_1.status = STARTED
            elif sound_1.isFinished:
                sound_1.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # check responses
        if keyResp.keys in ['', [], None]:  # No response was made
            keyResp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               keyResp.corr = 1;  # correct non-response
            else:
               keyResp.corr = 0;  # failed to respond (incorrectly)
        # store data for ExptLoop2 (TrialHandler)
        ExptLoop2.addData('keyResp.keys',keyResp.keys)
        ExptLoop2.addData('keyResp.corr', keyResp.corr)
        if keyResp.keys != None:  # we had a response
            ExptLoop2.addData('keyResp.rt', keyResp.rt)
            ExptLoop2.addData('keyResp.duration', keyResp.duration)
        # store data for ExptLoop2 (TrialHandler)
        ExptLoop2.addData('mouseResp.x', mouseResp.x)
        ExptLoop2.addData('mouseResp.y', mouseResp.y)
        ExptLoop2.addData('mouseResp.leftButton', mouseResp.leftButton)
        ExptLoop2.addData('mouseResp.midButton', mouseResp.midButton)
        ExptLoop2.addData('mouseResp.rightButton', mouseResp.rightButton)
        ExptLoop2.addData('mouseResp.time', mouseResp.time)
        ExptLoop2.addData('mouseResp.clicked_name', mouseResp.clicked_name)
        # Run 'End Routine' code from recordRTandAccuracy
        #this code is to record the reaction times and accuracy of the trial
        
        thisRoutineDuration = t # how long did this trial last
        
        # keyResp.rt is the time with which a key was pressed
        # mouseResp.time is the time with which a button was clicked/pressed
        # thisRecRT - how long it took for participants to respond after onset of targetImage
        # thisRespType - keeping track of which response component was used
        # thisAcc - whether or not the response was correct
        # correctMouseResp - name of column in data output which records the accuracy of mouse responses
        
        if keyResp.keys:
            thisRespType = 'keyboard' #record type of response 
            thisRecRT = keyResp.rt - onsetTime #record time taken to response
            if keyResp.corr == 1: #if the response is correct
                thisAcc = 'correct' #print correct
            else:
                thisAcc = 'incorrect'
        else:
            thisRespType = 'mouse'
            thisRecRT = mouseResp.time[0] - onsetTime
            if mouseResp.clicked_name[0] == corrButtonName: #check if what was clicked corresponds to the correct button
                thisAcc = 'correct'
                thisExp.addData('correctMouseResp', 1) #record accuracy of mouse clicks
            else:
                thisAcc = 'incorrect'
                thisExp.addData('correctMouseResp', 0)
        
        thisExp.addData('trialRespTimes', thisRecRT) #record the actual response times of each trial
        
        
        #print(thisRoutineDuration, thisRecRT, thisRespType, thisAcc, onsetTime)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 100.0 repeats of 'ExptLoop2'
    
    
    # --- Prepare to start Routine "description_p3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('description_p3.started', globalClock.getTime())
    startInst_4.keys = []
    startInst_4.rt = []
    _startInst_4_allKeys = []
    # setup some python lists for storing info about the startMouse_4
    gotValidClick = False  # until a click is received
    startMouse_4.mouseClock.reset()
    # keep track of which components have finished
    description_p3Components = [instr_4, startInst_4, startMouse_4]
    for thisComponent in description_p3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "description_p3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_4* updates
        
        # if instr_4 is starting this frame...
        if instr_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_4.frameNStart = frameN  # exact frame index
            instr_4.tStart = t  # local t and not account for scr refresh
            instr_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr_4.status = STARTED
            instr_4.setAutoDraw(True)
        
        # if instr_4 is active this frame...
        if instr_4.status == STARTED:
            # update params
            pass
        
        # *startInst_4* updates
        waitOnFlip = False
        
        # if startInst_4 is starting this frame...
        if startInst_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startInst_4.frameNStart = frameN  # exact frame index
            startInst_4.tStart = t  # local t and not account for scr refresh
            startInst_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startInst_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'startInst_4.started')
            # update status
            startInst_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(startInst_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(startInst_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if startInst_4.status == STARTED and not waitOnFlip:
            theseKeys = startInst_4.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
            _startInst_4_allKeys.extend(theseKeys)
            if len(_startInst_4_allKeys):
                startInst_4.keys = _startInst_4_allKeys[-1].name  # just the last key pressed
                startInst_4.rt = _startInst_4_allKeys[-1].rt
                startInst_4.duration = _startInst_4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # *startMouse_4* updates
        
        # if startMouse_4 is starting this frame...
        if startMouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startMouse_4.frameNStart = frameN  # exact frame index
            startMouse_4.tStart = t  # local t and not account for scr refresh
            startMouse_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startMouse_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('startMouse_4.started', t)
            # update status
            startMouse_4.status = STARTED
            prevButtonState = startMouse_4.getPressed()  # if button is down already this ISN'T a new click
        if startMouse_4.status == STARTED:  # only update if started and not finished!
            buttons = startMouse_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in description_p3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "description_p3" ---
    for thisComponent in description_p3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('description_p3.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "description_p3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    ExptLoop3 = data.TrialHandler(nReps=100.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('RTtimeConditions_main.xlsx'),
        seed=None, name='ExptLoop3')
    thisExp.addLoop(ExptLoop3)  # add the loop to the experiment
    thisExptLoop3 = ExptLoop3.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisExptLoop3.rgb)
    if thisExptLoop3 != None:
        for paramName in thisExptLoop3:
            globals()[paramName] = thisExptLoop3[paramName]
    
    for thisExptLoop3 in ExptLoop3:
        currentLoop = ExptLoop3
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisExptLoop3.rgb)
        if thisExptLoop3 != None:
            for paramName in thisExptLoop3:
                globals()[paramName] = thisExptLoop3[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime())
        # Run 'Begin Routine' code from setStimuli
        positionList = [-0.375,-0.125,0.125,0.375] #list of possible X coordinates for target to appear
        shuffle(positionList) #randomise these positions
        targetX = positionList[0] #pick the first value from the list 
        
        #thisImage is the variable in the Image field of targetImage
        if thisImage == 'images/red_dot.png': #path of where to find the target image
            corrAns = 'c' #setting the key press that will be the correct answer
            corrButton = red_button #setting the button that will be the correct answer
            corrButtonName = 'red_button' #making this a string so that it can be compared later when checking for acccuracy
        elif thisImage == 'images/green_dot.png':
            corrAns = 'v'
            corrButton = green_button
            corrButtonName = 'green_button'
        elif thisImage == 'images/blue_dot.png':
            corrAns = 'b'
            corrButton = blue_button
            corrButtonName = 'blue_button'
        
        
        targetImage.setPos([targetX, 0])
        targetImage.setImage(thisImage)
        keyResp.keys = []
        keyResp.rt = []
        _keyResp_allKeys = []
        # setup some python lists for storing info about the mouseResp
        mouseResp.x = []
        mouseResp.y = []
        mouseResp.leftButton = []
        mouseResp.midButton = []
        mouseResp.rightButton = []
        mouseResp.time = []
        mouseResp.clicked_name = []
        gotValidClick = False  # until a click is received
        mouseResp.mouseClock.reset()
        sound_1.setSound('G:/Mon Drive/school/2-master/M1/S2/TER/Projet/son/Deep Sleep [3.0Hz Delta Waves] Binaural Beats & Rain Sounds & music.wav', secs=600, hamming=True)
        sound_1.setVolume(1.0, log=False)
        sound_1.seek(0)
        # keep track of which components have finished
        trialComponents = [rightright_tile, right_tile, left_tile, leftleft_tile, red_button, green_button, blue_button, targetImage, keyResp, mouseResp, sound_1]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rightright_tile* updates
            
            # if rightright_tile is starting this frame...
            if rightright_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                rightright_tile.frameNStart = frameN  # exact frame index
                rightright_tile.tStart = t  # local t and not account for scr refresh
                rightright_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rightright_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                rightright_tile.status = STARTED
                rightright_tile.setAutoDraw(True)
            
            # if rightright_tile is active this frame...
            if rightright_tile.status == STARTED:
                # update params
                pass
            
            # *right_tile* updates
            
            # if right_tile is starting this frame...
            if right_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                right_tile.frameNStart = frameN  # exact frame index
                right_tile.tStart = t  # local t and not account for scr refresh
                right_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                right_tile.status = STARTED
                right_tile.setAutoDraw(True)
            
            # if right_tile is active this frame...
            if right_tile.status == STARTED:
                # update params
                pass
            
            # *left_tile* updates
            
            # if left_tile is starting this frame...
            if left_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                left_tile.frameNStart = frameN  # exact frame index
                left_tile.tStart = t  # local t and not account for scr refresh
                left_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                left_tile.status = STARTED
                left_tile.setAutoDraw(True)
            
            # if left_tile is active this frame...
            if left_tile.status == STARTED:
                # update params
                pass
            
            # *leftleft_tile* updates
            
            # if leftleft_tile is starting this frame...
            if leftleft_tile.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                leftleft_tile.frameNStart = frameN  # exact frame index
                leftleft_tile.tStart = t  # local t and not account for scr refresh
                leftleft_tile.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(leftleft_tile, 'tStartRefresh')  # time at next scr refresh
                # update status
                leftleft_tile.status = STARTED
                leftleft_tile.setAutoDraw(True)
            
            # if leftleft_tile is active this frame...
            if leftleft_tile.status == STARTED:
                # update params
                pass
            
            # *red_button* updates
            
            # if red_button is starting this frame...
            if red_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                red_button.frameNStart = frameN  # exact frame index
                red_button.tStart = t  # local t and not account for scr refresh
                red_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(red_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                red_button.status = STARTED
                red_button.setAutoDraw(True)
            
            # if red_button is active this frame...
            if red_button.status == STARTED:
                # update params
                pass
            
            # *green_button* updates
            
            # if green_button is starting this frame...
            if green_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                green_button.frameNStart = frameN  # exact frame index
                green_button.tStart = t  # local t and not account for scr refresh
                green_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(green_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                green_button.status = STARTED
                green_button.setAutoDraw(True)
            
            # if green_button is active this frame...
            if green_button.status == STARTED:
                # update params
                pass
            
            # *blue_button* updates
            
            # if blue_button is starting this frame...
            if blue_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                blue_button.frameNStart = frameN  # exact frame index
                blue_button.tStart = t  # local t and not account for scr refresh
                blue_button.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blue_button, 'tStartRefresh')  # time at next scr refresh
                # update status
                blue_button.status = STARTED
                blue_button.setAutoDraw(True)
            
            # if blue_button is active this frame...
            if blue_button.status == STARTED:
                # update params
                pass
            
            # *targetImage* updates
            
            # if targetImage is starting this frame...
            if targetImage.status == NOT_STARTED and tThisFlip >= onsetTime-frameTolerance:
                # keep track of start time/frame for later
                targetImage.frameNStart = frameN  # exact frame index
                targetImage.tStart = t  # local t and not account for scr refresh
                targetImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(targetImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'targetImage.started')
                # update status
                targetImage.status = STARTED
                targetImage.setAutoDraw(True)
            
            # if targetImage is active this frame...
            if targetImage.status == STARTED:
                # update params
                pass
            
            # if targetImage is stopping this frame...
            if targetImage.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > targetImage.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    targetImage.tStop = t  # not accounting for scr refresh
                    targetImage.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'targetImage.stopped')
                    # update status
                    targetImage.status = FINISHED
                    targetImage.setAutoDraw(False)
            
            # *keyResp* updates
            
            # if keyResp is starting this frame...
            if keyResp.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                keyResp.frameNStart = frameN  # exact frame index
                keyResp.tStart = t  # local t and not account for scr refresh
                keyResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
                # update status
                keyResp.status = STARTED
                # keyboard checking is just starting
                keyResp.clock.reset()  # now t=0
                keyResp.clearEvents(eventType='keyboard')
            if keyResp.status == STARTED:
                theseKeys = keyResp.getKeys(keyList=['b','c','v'], ignoreKeys=["escape"], waitRelease=False)
                _keyResp_allKeys.extend(theseKeys)
                if len(_keyResp_allKeys):
                    keyResp.keys = _keyResp_allKeys[-1].name  # just the last key pressed
                    keyResp.rt = _keyResp_allKeys[-1].rt
                    keyResp.duration = _keyResp_allKeys[-1].duration
                    # was this correct?
                    if (keyResp.keys == str(corrAns)) or (keyResp.keys == corrAns):
                        keyResp.corr = 1
                    else:
                        keyResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # *mouseResp* updates
            
            # if mouseResp is starting this frame...
            if mouseResp.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                mouseResp.frameNStart = frameN  # exact frame index
                mouseResp.tStart = t  # local t and not account for scr refresh
                mouseResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouseResp, 'tStartRefresh')  # time at next scr refresh
                # update status
                mouseResp.status = STARTED
                prevButtonState = mouseResp.getPressed()  # if button is down already this ISN'T a new click
            if mouseResp.status == STARTED:  # only update if started and not finished!
                buttons = mouseResp.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([square_button, plus_button, cross_button], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouseResp):
                                gotValidClick = True
                                mouseResp.clicked_name.append(obj.name)
                        x, y = mouseResp.getPos()
                        mouseResp.x.append(x)
                        mouseResp.y.append(y)
                        buttons = mouseResp.getPressed()
                        mouseResp.leftButton.append(buttons[0])
                        mouseResp.midButton.append(buttons[1])
                        mouseResp.rightButton.append(buttons[2])
                        mouseResp.time.append(mouseResp.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
            # if sound_1 is starting this frame...
            if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                sound_1.frameNStart = frameN  # exact frame index
                sound_1.tStart = t  # local t and not account for scr refresh
                sound_1.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('sound_1.started', tThisFlipGlobal)
                # update status
                sound_1.status = STARTED
                sound_1.play(when=win)  # sync with win flip
            
            # if sound_1 is stopping this frame...
            if sound_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > sound_1.tStartRefresh + 600-frameTolerance:
                    # keep track of stop time/frame for later
                    sound_1.tStop = t  # not accounting for scr refresh
                    sound_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'sound_1.stopped')
                    # update status
                    sound_1.status = FINISHED
                    sound_1.stop()
            # update sound_1 status according to whether it's playing
            if sound_1.isPlaying:
                sound_1.status = STARTED
            elif sound_1.isFinished:
                sound_1.status = FINISHED
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime())
        # check responses
        if keyResp.keys in ['', [], None]:  # No response was made
            keyResp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               keyResp.corr = 1;  # correct non-response
            else:
               keyResp.corr = 0;  # failed to respond (incorrectly)
        # store data for ExptLoop3 (TrialHandler)
        ExptLoop3.addData('keyResp.keys',keyResp.keys)
        ExptLoop3.addData('keyResp.corr', keyResp.corr)
        if keyResp.keys != None:  # we had a response
            ExptLoop3.addData('keyResp.rt', keyResp.rt)
            ExptLoop3.addData('keyResp.duration', keyResp.duration)
        # store data for ExptLoop3 (TrialHandler)
        ExptLoop3.addData('mouseResp.x', mouseResp.x)
        ExptLoop3.addData('mouseResp.y', mouseResp.y)
        ExptLoop3.addData('mouseResp.leftButton', mouseResp.leftButton)
        ExptLoop3.addData('mouseResp.midButton', mouseResp.midButton)
        ExptLoop3.addData('mouseResp.rightButton', mouseResp.rightButton)
        ExptLoop3.addData('mouseResp.time', mouseResp.time)
        ExptLoop3.addData('mouseResp.clicked_name', mouseResp.clicked_name)
        # Run 'End Routine' code from recordRTandAccuracy
        #this code is to record the reaction times and accuracy of the trial
        
        thisRoutineDuration = t # how long did this trial last
        
        # keyResp.rt is the time with which a key was pressed
        # mouseResp.time is the time with which a button was clicked/pressed
        # thisRecRT - how long it took for participants to respond after onset of targetImage
        # thisRespType - keeping track of which response component was used
        # thisAcc - whether or not the response was correct
        # correctMouseResp - name of column in data output which records the accuracy of mouse responses
        
        if keyResp.keys:
            thisRespType = 'keyboard' #record type of response 
            thisRecRT = keyResp.rt - onsetTime #record time taken to response
            if keyResp.corr == 1: #if the response is correct
                thisAcc = 'correct' #print correct
            else:
                thisAcc = 'incorrect'
        else:
            thisRespType = 'mouse'
            thisRecRT = mouseResp.time[0] - onsetTime
            if mouseResp.clicked_name[0] == corrButtonName: #check if what was clicked corresponds to the correct button
                thisAcc = 'correct'
                thisExp.addData('correctMouseResp', 1) #record accuracy of mouse clicks
            else:
                thisAcc = 'incorrect'
                thisExp.addData('correctMouseResp', 0)
        
        thisExp.addData('trialRespTimes', thisRecRT) #record the actual response times of each trial
        
        
        #print(thisRoutineDuration, thisRecRT, thisRespType, thisAcc, onsetTime)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 100.0 repeats of 'ExptLoop3'
    
    
    # --- Prepare to start Routine "end_message" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end_message.started', globalClock.getTime())
    # keep track of which components have finished
    end_messageComponents = [end_text]
    for thisComponent in end_messageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_message" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_text* updates
        
        # if end_text is starting this frame...
        if end_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            end_text.frameNStart = frameN  # exact frame index
            end_text.tStart = t  # local t and not account for scr refresh
            end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            end_text.status = STARTED
            end_text.setAutoDraw(True)
        
        # if end_text is active this frame...
        if end_text.status == STARTED:
            # update params
            pass
        
        # if end_text is stopping this frame...
        if end_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_text.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                end_text.tStop = t  # not accounting for scr refresh
                end_text.frameNStop = frameN  # exact frame index
                # update status
                end_text.status = FINISHED
                end_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_messageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_message" ---
    for thisComponent in end_messageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end_message.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
