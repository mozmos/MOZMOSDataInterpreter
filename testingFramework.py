###Test Data generator
#Original algorithm written by the MOZMOS Group
from random import randint, uniform

class dataGen:
    def allData():
        ph = dataGen.ph()
        temperature = dataGen.temperature()
        ppm = dataGen.ppm()
        time = dataGen.time()

        data = []
        data.append(ph)
        data.append(temperature)
        data.append(ppm)
        data.append(time)

        dataGen.writeFile(data)

    def ph():
        dataarray = []
        for i in range(100):
            number = 7
            dataarray.append(number)
        return dataarray
    
    def temperature():
        dataarray = []
        for i in range(100):
            number = randint(19,24)
            dataarray.append(number)
        return dataarray

    def ppm():
        dataarray = []
        for i in range(100):
            number = randint(1100,1200)
            dataarray.append(number)
        return dataarray

    def time():
        dataarray = []
        for i in range(100):
            number = i
            dataarray.append(number)
        return dataarray

    def writeFile(data):
        file = open("generatedTestData.txt", "w+")
        i = 0
        while i < len(data[0]):
            file.write(str(data[0][i]) + "\n")
            file.write(str(data[1][i]) + "\n")
            file.write(str(data[2][i]) + "\n")
            file.write(str(data[3][i]) + "\n")
            i += 1
        file.close()