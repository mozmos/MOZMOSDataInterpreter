#Main Window
WIDTH = 1280
HEIGHT = int(WIDTH * 0.5625)
TITLE = "MOZMOS DataConnect"
DATA_AMOUNT = 4

#Dynamic Items
removedDataLength = 0
dataCounter = 0

#Graph
GRAPH_TITLE = "Collected Data"
GRAPH_WIDTH = 10
GRAPH_HEIGHT = 5
YAXIS = [0,100]
LINE_COLOURS = ['blue', 'orange', 'green']

#Settings Page
SETTINGS_WIDTH = 400
SETTINGS_HEIGHT = SETTINGS_WIDTH
SETTINGS_TITLE = "Settings"

#Settings in Settings Page
Main_Settings = ['Themes', 'Graph', "Language", "Accessibility"]

#Graph Settings
DarkGray = (0.160784314,0.160784314,0.160784314)
desert = (1,210/255,112/255)
desert2 = (96/255,73/255,26/255)
lightblue = (145/255,182/255,1)
mozblue = (0,1,1)
COLOURS = ['Blue', 'Green', 'Red', 'Cyan', 'Magenta', 'Yellow', DarkGray, 'White', 'Black', desert, desert2, lightblue, mozblue] #13 elements
THEMES = ['Light', 'Dark', 'Desert', 'Oceanic', 'MOZ-Theme']
CURRENT_THEME = 'Light'
themeAttributes = [[COLOURS[8],COLOURS[8],COLOURS[8],COLOURS[8],COLOURS[8],COLOURS[8],COLOURS[8],COLOURS[8],COLOURS[8],COLOURS[7],COLOURS[7]],
                    [COLOURS[7],COLOURS[7],COLOURS[7],COLOURS[7],COLOURS[7],COLOURS[7],COLOURS[7],COLOURS[7],COLOURS[7],COLOURS[6],COLOURS[6]],
                    [COLOURS[10],COLOURS[10],COLOURS[10],COLOURS[10],COLOURS[10],COLOURS[10],COLOURS[10],COLOURS[10],COLOURS[10],COLOURS[9],COLOURS[9]],
                    [COLOURS[8],COLOURS[0],COLOURS[0],COLOURS[0],COLOURS[0],COLOURS[11],COLOURS[11],COLOURS[8],COLOURS[8],COLOURS[11],COLOURS[11]],
                    [COLOURS[7],COLOURS[12],COLOURS[12],COLOURS[12],COLOURS[12],COLOURS[12],COLOURS[12],COLOURS[12],COLOURS[12],COLOURS[8],COLOURS[8]]
                    ] ##[outline, background, title colour, ]
                    
