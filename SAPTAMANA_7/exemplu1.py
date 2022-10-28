import pandas as pd
# a = [1,7,2]
# variabila = pd.Series(a, index=["x","y","z"])
# print(variabila)

# taskuri = {"ziua1":2, "ziua2":4, "ziua3":1}
# variabila= pd.Series(taskuri)
# print(variabila)

# taskuri = {"ziua1":2, "ziua2":4, "ziua3":1}
# variabila= pd.Series(taskuri, index=["ziua2"])
# # print(variabila)
#
# taskuri = {
#     "zile":[2,4,5],
#     "durata":[50,40,45]
# }
# variabila=pd.DataFrame(taskuri)
# print(variabila)

# variabila=pd.DataFrame(taskuri, index=["ziua1", "ziua2", "ziua3"])
# variabila['zile'].loc[1]=50
# print(variabila)
# print(variabila.loc[0])
# print(variabila.loc[[0,1]])
# print(variabila.loc["ziua1":"ziua2"])

'''Metoda de importare a fisierului date_test.csv in program'''
variabila = pd.read_csv('date_test.csv')
print(variabila)

