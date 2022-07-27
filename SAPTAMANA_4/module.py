#from test import test_function
#from test import *
#import test
import sys

var_1 = 10
var_2 = 20
var_3 = 30

#result_modul = test_function(var_1, var_2, var_3)
#print(result_modul)
#print(test.ionel)

import sys, os
print(sys.path)
BASE = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
print(os.path.abspath(__file__))
PRINT(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

#from SAPTAMANA_3.Functii import test_function
#result_modul = test_function(var_1, var_2, var_3)
#print(result_modul)
