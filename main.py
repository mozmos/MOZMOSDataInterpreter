from tkinter import *
import settings
from settings import *
import matplotlib as graphTool
from matplotlib import pyplot as graphEditor
from matplotlib import FigureCanvasTkAgg
from importFile import *

master = Tk()

master.title = TITLE

class Init:
    def setup():
        Init.buttons()
    
    def buttons():
        loadFile = Button(master, text = "Load File", command = Commands.load).place(x = 20, y = 50)
        allDataPoints = Button(master, text = "View All Data Points", command = lambda: Commands.filterData("all")).place(x = 20, y = 150)
        ph = Button(master, text = "View pH Levels", command = lambda: Commands.filterData("ph")).place(x = 20, y = 180)
        temperature = Button(master, text = "View Temperature Levels", command = lambda: Commands.filterData("temp")).place(x = 20, y = 210)
        ppm = Button(master, text = "View PPM Levels", command = lambda: Commands.filterData("ppm")).place(x = 20, y = 240)

class Commands:
    ##Loads the file
    def load():
        fileSuccess = False
        print("Loading file...")
        file = FileImport.importfile()
        if file != "failed":
            fileSuccess = True
        
        if fileSuccess:
            file = open(file, "r")
            Commands.decodeData(file)
    
    #STUB - filters the graph by data type
    def filterData(filter):
        print(filter)
    
    #Decodes the text file and formats it properly
    def decodeData(file):
        oldData = file.readlines()
        repairedData = []
        data = []
        #remove unnecessary data
        for dataItem in oldData:
            dataItem = dataItem.strip("\n")
            repairedData.append(dataItem)
        tempData = []

        #Check if data is complete
        if (len(repairedData) % DATA_AMOUNT) == 0:
            print("Data is adequate!")
        elif ((len(repairedData) - 1) % DATA_AMOUNT) == 0:
            print("Data is adequate! Removed 1 data piece")
            settings.removedDataLength += 1
        elif ((len(repairedData) - 2) % DATA_AMOUNT) == 0:
            print("Data is adequate! Removed 2 data pieces")
            settings.removedDataLength += 2
        elif ((len(repairedData) - 3) % DATA_AMOUNT) == 0:
            print("Data is adequate! Removed 3 data pieces")
            settings.removedDataLength += 3
        
        ##Remove the excess data that is unneeded
        for i in range(0,settings.removedDataLength):
            repairedData.remove(repairedData[(len(repairedData) - 1) - i])

        ##Split the data into groups of 4 to represent the different pieces of data
        for i in range(0,len(repairedData)):
            dataPiece = repairedData[i]
            tempData.append(dataPiece)
            if settings.dataCounter == 3:
                data.append(tempData)
                settings.dataCounter = 0
                tempData = []
            else:
                settings.dataCounter += 1


class Graph:
    def init():
        graphTool.use("TkAgg")

    def graph_draw():
        x1 = [10,20,30]
        y1 = [20,40,60]

        graphEditor.plot(x1, y1, label = "line")
        
        x2 = [15,25,35]
        y2 = [40, 10, 30]

        graphEditor.plot(x2, y2, label = "line 2")
        graphEditor.xlabel('x-axis')
        graphEditor.ylabel('y-axis')
        graphEditor.title(GRAPH_TITLE)
        graphEditor.legend()
        graphEditor.show()

##Run window and setup
Init.setup()
Graph.graph_draw()
master.geometry(f"{WIDTH}x{HEIGHT}")
master.resizable(width = False, height = False)
master.mainloop()