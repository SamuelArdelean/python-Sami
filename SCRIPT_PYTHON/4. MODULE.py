#MODULELE ne ajuta sa importam alte obiecte din alte fisiere ale aceluiasi folder
'''VARIANTA 1 DE IMPORT'''
# from test_module import test_function, ionel    #* - importa toate obiectele din celalalt fisier
#
# var_1 = 10
# var_2 = 20
# var_3 = 30
#
# result_modul = test_function(var_1,var_2, var_3)
# print(result_modul)
# print(ionel)

'''VARIANTA 2 DE IMPORT'''
# import test_module
var_1 = 10
var_2 = 20
var_3 = 30
#
# result_modul = test_module.test_function(var_1,var_2, var_3)
# print(result_modul)
# print(test_module.ionel)


#PACHETE  -   putem importa obicte din alte foldere
import sys, os  #variabile sistem
print(sys.path)
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #  merge inapoi inspre fisierul principal
sys.path.insert(0, BASE)

# print(sys.path)
#
# from SAPTAMANA_3.Functii import test_function
# result_modul = test_function(var_1,var_2,var_3)
# print(result_modul)