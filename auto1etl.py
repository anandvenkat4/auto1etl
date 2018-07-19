import sys
import locale
import json

class Auto1ETL:
    def __init__(self):
        try:
            with open('config.json', 'r') as config_file:
                self.config = json.load(config_file)
            config_file.close()
        except FileNotFoundError:
            print("The specified config file is not found. Please check the filename and try again")
        except:
            print("Unexpected error:", sys.exc_info()[0])
        
        try:
            with open(self.config['filename'], 'r') as data_file:
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
            self.dictColDef[item] = counter
            counter = counter + 1
        
        locale.setlocale(locale.LC_ALL, 'de_de')

        self.transformationFunctions = {
            'engine-location': (lambda x: 0 if x == self.config['engLocn'] else 1), 
            'num-of-cylinders': (lambda x: self.config['words2Num'][x]), 
            'engine-size': (lambda x: int(x)), 
            'weight': (lambda x: int(x)), 
            'horsepower': (lambda x: locale.atof(x)), 
            'aspiration': (lambda x: 0 if x == self.config['aspiration'] else 1), 
            'price': (lambda x: locale.atof(x)/100), 
            'make': (lambda x: str(x))
        }

        self.transformedData = []

    def transformData(self, line):
        splittedLine = line.split(self.config['sepChar'])
        tempList = []
        for item in self.config['order']:
            tempList.append(self.transformationFunctions[item](splittedLine[self.dictColDef[item]]))
            
        self.transformedData.append(tempList)

    def loadAndTransform(self):
        with open(self.config['filename']) as dataTransform:
            next(dataTransform)
            for line in dataTransform:
                if self.config['NAChar'] in line:
                    continue
                self.transformData(line.strip())
        return [self.config['order']] + self.transformedData

if __name__ == "__main__":
    auto1etl = Auto1ETL()
    data = auto1etl.loadAndTransform()
    print(data)