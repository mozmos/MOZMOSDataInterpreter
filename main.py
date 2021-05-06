from tkinter import *
import settings
from settings import *
import matplotlib as graphTool
import matplotlib as plt
from matplotlib import pyplot as graphEditor
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from importFile import *
import numpy as np

root = Tk()

root.title = TITLE

class Init:
    def setup():
        Init.buttons()
    
    def buttons():
        loadFile = Button(root, text = "Load File", command = Commands.load).place(x = 20, y = 50)
        allDataPoints = Button(root, text = "View All Data Points", command = lambda: Commands.filterData("all")).place(x = 20, y = 150)
        ph = Button(root, text = "View pH Levels", command = lambda: Commands.filterData("ph")).place(x = 20, y = 180)
        temperature = Button(root, text = "View Temperature Levels", command = lambda: Commands.filterData("temp")).place(x = 20, y = 210)
        ppm = Button(root, text = "View PPM Levels", command = lambda: Commands.filterData("ppm")).place(x = 20, y = 240)

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
        pHArray = []
        temperatureArray = []
        ppmArray = []
        timeArray = [] #sorted array

        for i in range(0,len(repairedData)):
            dataPiece = repairedData[i]
            print(settings.dataCounter)
            if settings.dataCounter == 0: #ph
                pHArray.append(dataPiece)
            if settings.dataCounter == 1: #ph
                temperatureArray.append(dataPiece)
            if settings.dataCounter == 2: #ph
                ppmArray.append(dataPiece)
            if settings.dataCounter == 3:
                timeArray.append(dataPiece)
                settings.dataCounter = 0
            else:
                settings.dataCounter += 1

        data.append(pHArray)
        data.append(temperatureArray)
        data.append(ppmArray)
        print(data)
        
        #Graph Data
        #Graph.graph_draw([[50,20,24,53,17]])
        Graph.graph_draw(data, timeArray)

    def checkdatatype(mainArray, partOfArray, mainArrayLength):
        for i in range(0, mainArrayLength):
            if i == 0 and mainArray[i] == partOfArray:
                return "pH"
            elif i == 1 and mainArray[i] == partOfArray:
                return "Temperature"
            elif i == 2 and mainArray[i] == partOfArray:
                return "Salinity"

class Graph:
    def init():
        graphTool.use("TkAgg")

    def graph_draw(data, timerange):
        f = Figure(figsize = (GRAPH_WIDTH,GRAPH_HEIGHT), dpi=100)
        a = f.add_subplot(111)
        for dataArray in data:
            dataLabel = Commands.checkdatatype(data, dataArray, len(data))
            dataArray = list(map(int, dataArray))
            a.plot(timerange, dataArray, label = dataLabel)

        f.suptitle("Data Collected")

        canvas = FigureCanvasTkAgg(f, root)
        a.legend()
        canvas.get_tk_widget().place(x = 200, y = 10)

##Run window and setup
Init.setup()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(width = False, height = False)
root.mainloop()