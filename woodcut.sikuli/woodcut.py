from time import gmtime, strftime

Settings.MoveMouseDelay = 0
running = True
packEmpty = True
treeStillUp = True
atBank = True

def logThis(message):
    switchApp("TextEdit")
    paste("\n")
    if message != "\n":
        paste("{0}: {1}".format(strftime("%H:%M:%S", gmtime()), message))
    switchApp("App")

def runHotkey(event):
    logThis('    global running')
    global running
    logThis('    Running = false')
    running = False

def getWindow():
    find("1528758625915.png")
    click("1528758625915.png")

def areWeAtBank():
    logThis('    global atBank')
    global atBank
    if(exists("1528755597102.png")):
        logThis('        True')
        atBank = True
    else:
        logThis('        False')
        atBank = False

def fromBank():
    logThis('    finding tree')
    wait("1528755597102.png")
    logThis('    clicking tree - moving from bank')
    click(Pattern("1528755597102.png").targetOffset(-387,259))
    doubleClick(Pattern("1528755597102.png").targetOffset(-387,259))
    logThis('    wait(9)')
    wait(9)

def clickTree():
    logThis('    finding tree')
    find(Pattern("1528842326792.png").similar(0.50))
    click(Pattern("1528842326792.png").similar(0.50).targetOffset(402,26))
    doubleClick(Pattern("1528842326792.png").similar(0.50).targetOffset(402,26))
    hover(Pattern("1528842326792.png").similar(0.50).targetOffset(405,290))
    logThis('    clicking tree')
    logThis('    doubleclick tree')

def backpackFull():
    logThis('    global packEmpty')
    global packEmpty
    if(exists(Pattern("1528759332914.png").similar(0.98))):
        logThis('        False')
        packEmpty = False
    else:
        logThis('        True')
        packEmpty = True

def checkTree():
    logThis('    global treeStillUp')
    global treeStillUp
    if(exists(Pattern("1529171340151.png").similar(0.55))):
        logThis('        True')
        treeStillUp = True
    else:
        logThis('        False')
        treeStillUp = False

def bankLogs():
    logThis('    finding bank')
    find(Pattern("1528838305119.png").similar(0.58))
    logThis('    click bank')
    click(Pattern("1528838305119.png").similar(0.58).targetOffset(35,-42))
    logThis('    double click bank')
    doubleClick(Pattern("1528838305119.png").similar(0.58).targetOffset(35,-42))
    logThis('    wait(9)')
    wait(9.0)
    logThis('    finding bank tab')
    find(Pattern("1528759436235.png").similar(0.45))
    logThis('    click deposit')
    click(Pattern("1528759436235.png").similar(0.45).targetOffset(60,552))
    logThis('    wait(1)')
    wait(1)
    logThis('    click close bank tab')
    click(Pattern("1528759436235.png").similar(0.45).targetOffset(165,-1))

Env.addHotkey("c", KeyModifier.CTRL, runHotkey)

switchApp("App")
getWindow()
while(running):
    logThis('\n')
    if(running):
        logThis('Are we at Bank?')
        areWeAtBank()
        logThis('Back pack full? - 1')
        backpackFull()
    if(atBank):
        logThis('Travelling from bank')
        logThis('Getting window')
        getWindow()
        fromBank()
    while(packEmpty and running):
        logThis('\n')
        logThis('While pack empty')
        if(running):
            logThis('checking tree')
            checkTree()
        if(treeStillUp and running):
            logThis('\n')
            logThis('If - Tree is there ...')
            logThis('Click tree')
            clickTree()
            while(packEmpty and treeStillUp and running):
                logThis('\n')
                logThis('Currently Cutting ...')
                if(running):
                    logThis('Back pack full? - 2')
                    backpackFull()
                    logThis('checking tree')
                    checkTree()
    if(running):
        logThis('\n')
        logThis('Banking Logs')
        logThis('Getting window')
        getWindow()
bankLogs()
