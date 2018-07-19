"""Module for Loading and Transformation of the given data file

Owner: Venkateshwaran Loganathan
Created: 19 July 2018"""

#import necessary modules
import sys
import os
import locale
import json

class Auto1ETL:
    """ Class used for the loading and transformation of the given data set"""
    def __init__(self, filePath=''):
        """Contructor that initializes various parameters used in the module"""
        #Identifies the current directory of this file
        self.currDir = os.path.dirname(os.path.realpath(__file__)) 
        self.filePath = filePath
        try:
            '''Loading the config file.
            //TODO: Can be extracted from environment variable settings as well
            '''
            with open(self.currDir + '/' + 'config.json', 'r') as config_file:
                self.config = json.load(config_file)
            config_file.close()
        except FileNotFoundError:
            print("The specified config file is not found. Please check the filename and try again")
        except:
            print("Unexpected error:", sys.exc_info()[0])
        
        try:
            if self.filePath == '':
                self.filePath = self.currDir + '/' + self.config['inputDataFile']
            with open(self.filePath, 'r') as data_file:
                #Getting the first line to identify the columns in the given data file. The sepChar is a configurable parameter
                self.colDef = data_file.readline().strip().split(self.config['sepChar'])
            data_file.close()
        except AttributeError:
            print("The config attribute is missing. Please check and try again")
        except FileNotFoundError:
            print("The specified data input file is not found. Please check the filename and try again")
        except:
            print("Unexpected error:", sys.exc_info()[0])

        counter = 0
        self.dictColDef = {}
        for item in self.colDef :
            #Setting up the column headers definition
            self.dictColDef[item] = counter
            counter = counter + 1
        
        #Setting the locale to German, this takes care of utf-8 and german digit settings
        locale.setlocale(locale.LC_ALL, self.config['locale'])

        #Series of lambda functions that transforms the data into the specified format given in the problem statement
        self.transformationFunctions = {
            'engine-location': (lambda x: 0 if x == self.config['engLocn'] else 1), #Coding engine location front to be 0 and rear to be 1
            'num-of-cylinders': (lambda x: self.config['words2Num'][x]), #Funtion to convert number names to numbers //TODO: can be extended and built as a separate functionality
            'engine-size': (lambda x: int(x)),  
            'weight': (lambda x: int(x)), 
            'horsepower': (lambda x: locale.atof(x)), #converting to float
            'aspiration': (lambda x: 0 if x == self.config['aspiration'] else 1), #Boolean representation of aspiration
            'price': (lambda x: locale.atof(x)/100), #conversion of cents to Euros
            'make': (lambda x: str(x)) #No Change :)
        }

        self.transformedData = []

    def transformData(self, line):
        """Transforms the data line by line by calling the respective lambda functions"""
        splittedLine = line.split(self.config['sepChar'])
        tempList = []
        for item in self.config['order']:
            tempList.append(self.transformationFunctions[item](splittedLine[self.dictColDef[item]]))
            
        self.transformedData.append(tempList)

    def loadAndTransform(self):
        """Executes the program line by line and convert them"""
        with open(self.filePath) as dataTransform:
            next(dataTransform)
            for line in dataTransform:
                if self.config['NAChar'] in line:
                    continue
                self.transformData(line.strip())
        #returns the converted data after adding the columns definition in the top
        return [self.config['order']] + self.transformedData

#if __name__ == "__main__":
    #auto1etl = Auto1ETL()