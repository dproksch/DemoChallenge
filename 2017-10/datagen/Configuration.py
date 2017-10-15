import json
import fileinput

class Configuration:
    def __init__(self, fileName):
        self.fileName = fileName

    direction = {'up','down','steady'}
    quality = {'good','bad','average'}

    def processConfiguration(self):
        with open(self.fileName,"r") as inputFile:
            jsonFile = json.load(inputFile)
            #
            # Get Plant Information
            #
            j = jsonFile['plantInfo']
            self.plantNumber = j['plantNumber']
            self.plantBoothCount = j['plantBoothCount']
            self.plantPostalCode = j['plantPostalCode']

            # get Temp/ Humidity Information
            j = jsonFile['environmentInfo']
            self.startingTemp = j['startingTemp']
            self.tempDirection = j['tempDirection']
            if self.tempDirection not in self.direction:
                raise LookupError("Expected {} found {}".format(self.direction, self.tempDirection))

            self.startingHumidity = j['startingHumidity']
            self.humidityDirection = j['humidityDirection']
            if self.humidityDirection not in self.direction:
                raise LookupError("Expected {} found {}".format(self.direction, self.humidityDirection))

            # get Air Information
            self.airFlow = j['airFlow']
            self.airPressureInside = j['airPressureInside']
            self.airPressureOutside = j['airPressureOutside']
            self.airPressureDirection = j['airPressureDirection']
            if self.airPressureDirection not in self.direction:
                raise LookupError("Expected {} found {}".format(self.direction, self.airPressureDirection))

            # get ppm / Filter Information
            j = jsonFile['airQualityInfo']
            self.ppm = j['ppm']
            self.ppmDirection = j['ppmDirection']
            self.filterQuality = j['filterQuality']
            if self.filterQuality not in self.quality:
                raise LookupError("Expected {} found {}".format(self.direction, self.humidityDirection))


            # get Date Information
            j = jsonFile['durationInfo']
            self.numberOfDays = j['numberofDays']
            self.startDate = j['startDate']
            self.ticks = int(j['ticks'])
            self.seed = int(j['seed'])
