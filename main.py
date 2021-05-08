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
import os

root = Tk()

root.title = TITLE

data = []
timeData = []
fileSuccess = False
icons = []
currentFilter = None

class Init:
    def setup():
        Init.buttons()
    
    def buttons():
        global icons
        icons = Init.loadIcons()

        allDataPoints = Button(root, image = icons[1], command = lambda: Commands.filterData("all"))
        allDataPoints.image = icons[1]
        allDataPoints['state'] = DISABLED
        allDataPoints.place(x = 20, y = 255)

        ph = Button(root, image = icons[2], command = lambda: Commands.filterData("ph"))
        ph.image = icons[2]
        ph['state'] = DISABLED
        ph.place(x = 20, y = 355)
        
        temperature = Button(root, image = icons[3], command = lambda: Commands.filterData("temp"))
        temperature.image = icons[3]
        temperature['state'] = DISABLED
        temperature.place(x = 20, y = 450)
        
        ppm = Button(root, image=icons[4], command = lambda: Commands.filterData("ppm"))
        ppm.image = icons[4]
        ppm['state'] = DISABLED
        ppm.place(x = 20, y = 540)

        buttons = [allDataPoints, ph, temperature, ppm]

        loadFile = Button(root, image = icons[0], command = lambda: Commands.load(buttons))
        loadFile.image = icons[0]
        loadFile.place(x = 20, y = 100)

    def loadIcons():
        icons = []
        currentdir = os.path.dirname(os.path.abspath(__file__))
        currentdir += '\icons'
        dirLength = len(os.listdir(currentdir))

        for icon in range(0, dirLength):
            img = PhotoImage(file = f"{currentdir}/{icon}.png")
            icons.append(img)

        return icons

class Commands:
    ##Loads the file
    def load(buttonArray):
        global fileSuccess
        print("Loading file...")
        file = FileImport.importfile()
        if file != "failed":
            fileSuccess = True
        if fileSuccess:
            file = open(file, "r")
            for button in buttonArray:
                button['state'] = ACTIVE
            Commands.decodeData(file)
    
    #STUB - filters the graph by data type
    def filterData(filter):
        global data, timeData, fileSuccess, currentFilter
        print(currentFilter)
        if fileSuccess:
            tempArray = []
            
            #data[0] is pH,
            #data[1] = temperature
            #data[2] = ppm
            #data[3] = time

            if filter == "all" or filter == None:
                graph = Graph.graph_draw(data, timeData)
                currentFilter = 'all'

            if filter == "ph":
                tempArray = []
                tempArray.append(data[0])
                graph = Graph.graph_draw(tempArray, timeData, LINE_COLOURS[0], "pH")
                currentFilter = 'ph'
            
            if filter == "temp":
                tempArray = []
                tempArray.append(data[1])
                graph = Graph.graph_draw(tempArray, timeData, LINE_COLOURS[1], "Temperature")
                currentFilter = 'temp'
            
            if filter == "ppm":
                tempArray = []
                tempArray.append(data[2])
                graph = Graph.graph_draw(tempArray, timeData, LINE_COLOURS[2], "Salinity")
                currentFilter = 'ppm'
            print(graph)
            return graph
        else:
            messagebox.showwarning("No File Loaded", "No file was loaded. Please load one for data to display")
 
    #Decodes the text file and formats it properly
    def decodeData(file):
        global data, timeData
        oldData = file.readlines()
        repairedData = []
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

        for i in range(0,len(repairedData)):
            dataPiece = repairedData[i]
            if settings.dataCounter == 0: #ph
                pHArray.append(dataPiece)
            if settings.dataCounter == 1: #ph
                temperatureArray.append(dataPiece)
            if settings.dataCounter == 2: #ph
                ppmArray.append(dataPiece)
            if settings.dataCounter == 3:
                timeData.append(dataPiece)
                settings.dataCounter = 0
            else:
                settings.dataCounter += 1

        data.append(pHArray)
        data.append(temperatureArray)
        data.append(ppmArray)
        
        #Graph Data
        #Graph.graph_draw([[50,20,24,53,17]])
        Graph.graph_draw(data, timeData)

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

    def graph_draw(data, timerange, *args, **args2):
        global icons
        filteredData = False
        #Initialise the graph
        f = Figure(figsize = (GRAPH_WIDTH,GRAPH_HEIGHT), dpi=100)
        a = f.add_subplot(111)
        #check for filter arguments
        if args:
            filteredData = True
            print("filteredData")
        if args2:
            print("filteredData2")
        
        #Load and display the data
        for dataArray in data:
            insertedTimeRange = timerange
            dataLabel = Commands.checkdatatype(data, dataArray, len(data))
            dataArray = list(map(int, dataArray))
            insertedTimeRange = list(map(int, insertedTimeRange))
            if not filteredData:
                a.plot(insertedTimeRange, dataArray, label = dataLabel)
            else:
                a.plot(insertedTimeRange, dataArray, color = args[0], label = args[1])

        f.suptitle("Data Collected")

        canvas = FigureCanvasTkAgg(f, root)
        a.legend()
        canvas.get_tk_widget().place(x = 250, y = 100)
        #f.savefig('figure.png')

        saveImg = Button(root, image = icons[5], command = Graph.saveGraph)
        saveImg.image = icons[5]
        saveImg.place(x =940, y = 625)

        print(f)
        return f
    
    def saveGraph():
        global currentFilter
        #Get the current graph
        savableGraph = Commands.filterData(currentFilter)
        #save graph
        if currentFilter == "all":
            savableGraph.savefig("Graph.png")
        elif currentFilter == "ph":
            savableGraph.savefig("Acidity.png")
        elif currentFilter == "temp":
            savableGraph.savefig("Temperature.png")
        elif currentFilter == "ppm":
            savableGraph.savefig("Salinity.png")

        

##Run window and setup
Init.setup()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(width = False, height = False)
root.mainloop()