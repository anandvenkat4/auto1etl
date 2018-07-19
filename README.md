# auto1etl
ETL Task given by Auto1

This module contains all the necessary files that are created as part of the solution of the given task.

Sample Program to call this module:

sample.py
---------
from auto1etl import auto1etl

autoetl = auto1etl.Auto1ETL("/Users/venkat/Documents/workspace/auto1etl/Challenge_me.txt")
data = autoetl.loadAndTransform()
print(data)

Sample Output of the Task: (For the given data)
-----------------------------------------------
[['engine-location', 'num-of-cylinders', 'engine-size', 'weight', 'horsepower', 'aspiration', 'price', 'make'], [0, 4, 109, 2, 102.3, 0, 13950.0, 'audi'], [0, 5, 136, 2, 115.5, 0, 17450.0, 'audi'], [0, 5, 136, 1, 110.79, 0, 17710.0, 'audi'], [0, 4, 108, 2, 101.26, 0, 16430.0, 'bmw'], [0, 4, 108, 0, 101.44, 0, 16925.0, 'bmw'], [0, 6, 164, 0, 121.38, 0, 21105.0, 'bmw'], [0, 3, 61, 2, 48.07, 0, 5151.0, 'chevrolet'], [0, 4, 90, 1, 68.5, 0, 6377.0, 'dodge'], [0, 4, 98, 1, 102.29, 1, 7957.0, 'dodge'], [0, 4, 90, 1, 68.37, 0, 6692.0, 'dodge'], [0, 4, 110, 0, 86.48, 0, 9095.0, 'honda'], [0, 4, 91, 1, 68.65, 0, 6795.0, 'mazda'], [0, 4, 91, 1, 68.22, 0, 6695.0, 'mazda'], [0, 4, 122, 1, 84.0, 0, 8845.0, 'mazda'], [0, 4, 122, 1, 84.39, 0, 10595.0, 'mazda'], [0, 4, 92, 2, 68.1, 0, 6189.0, 'mitsubishi'], [0, 4, 92, 2, 68.4, 0, 6669.0, 'mitsubishi'], [0, 4, 98, 1, 102.78, 1, 7689.0, 'mitsubishi'], [0, 4, 122, 3, 88.41, 0, 8499.0, 'mitsubishi'], [0, 4, 122, 1, 88.49, 0, 8189.0, 'mitsubishi'], [0, 4, 110, 1, 116.44, 1, 9279.0, 'mitsubishi'], [0, 4, 97, 1, 69.94, 0, 6649.0, 'nissan'], [0, 4, 97, 1, 69.65, 0, 6849.0, 'nissan'], [0, 4, 97, 1, 69.06, 0, 7299.0, 'nissan'], [0, 4, 97, 1, 69.36, 0, 7999.0, 'nissan'], [0, 4, 120, 0, 97.53, 0, 8949.0, 'nissan'], [0, 4, 120, 0, 97.82, 0, 9549.0, 'nissan'], [0, 6, 181, 0, 152.43, 0, 14399.0, 'nissan'], [0, 6, 181, 0, 152.47, 0, 13499.0, 'nissan'], [0, 6, 181, 3, 160.3, 0, 17199.0, 'nissan'], [0, 6, 181, 1, 160.94, 0, 18399.0, 'nissan'], [0, 4, 152, 0, 95.2, 1, 13200.0, 'peugot'], [0, 4, 120, 0, 95.5, 0, 15580.0, 'peugot'], [0, 4, 152, 0, 95.73, 1, 16900.0, 'peugot'], [0, 4, 120, 0, 97.73, 0, 16630.0, 'peugot'], [0, 4, 152, 0, 95.84, 1, 17950.0, 'peugot'], [0, 4, 90, 1, 68.16, 0, 5572.0, 'plymouth'], [0, 4, 98, 1, 102.53, 1, 7957.0, 'plymouth'], [0, 4, 90, 1, 68.02, 0, 6692.0, 'plymouth'], [0, 4, 121, 2, 110.5, 0, 12170.0, 'saab'], [0, 4, 121, 3, 160.99, 0, 15040.0, 'saab'], [0, 4, 121, 3, 69.07, 1, 18150.0, 'saab'], [0, 4, 108, 2, 82.19, 0, 7053.0, 'subaru'], [0, 4, 108, 2, 82.6, 0, 7603.0, 'subaru'], [0, 4, 108, 0, 94.77, 0, 7126.0, 'subaru'], [0, 4, 108, 0, 82.78, 0, 7775.0, 'subaru'], [0, 4, 108, 0, 111.37, 0, 9960.0, 'subaru'], [0, 4, 108, 0, 94.6, 1, 11259.0, 'subaru'], [0, 4, 108, 0, 82.56, 0, 7463.0, 'subaru'], [0, 4, 108, 0, 111.5, 0, 10198.0, 'subaru'], [0, 4, 108, 0, 62.67, 1, 11694.0, 'subaru'], [0, 4, 92, 1, 62.23, 0, 6338.0, 'toyota'], [0, 4, 92, 1, 62.46, 0, 6488.0, 'toyota'], [0, 4, 92, 0, 70.55, 0, 7898.0, 'toyota'], [0, 4, 98, 0, 56.29, 0, 6938.0, 'toyota'], [0, 4, 98, 0, 56.62, 0, 7198.0, 'toyota'], [0, 4, 110, 0, 70.99, 0, 7898.0, 'toyota'], [0, 4, 98, 1, 112.38, 0, 8058.0, 'toyota'], [0, 4, 98, 1, 112.71, 0, 8238.0, 'toyota'], [0, 4, 146, 2, 116.22, 0, 9639.0, 'toyota'], [0, 4, 146, 2, 92.84, 0, 11549.0, 'toyota'], [0, 4, 146, 2, 73.83, 0, 17669.0, 'toyota'], [0, 6, 171, 3, 156.63, 0, 16558.0, 'toyota'], [0, 4, 109, 2, 68.41, 0, 8195.0, 'volkswagen'], [0, 4, 97, 2, 90.4, 1, 9495.0, 'volkswagen'], [0, 4, 109, 2, 90.9, 0, 9995.0, 'volkswagen'], [0, 4, 109, 3, 68.67, 0, 9980.0, 'volkswagen']]

Design Considerations:
----------------------

1. This module was created and tested in Python 3.5 using Anaconda environment setup
2. No external libraries/pip installations were used
3. The order of the columns are maintained in the same way as specified. The order is set in the config file whoch can be modified to include/change/delete the columns included. They are automatically re-generated. 
4. Locale settings were used to import German Language Settings
5. The unclean data lines are omitted
6. The versioning is maintained by git
7. Separation character is configurable from the config file


