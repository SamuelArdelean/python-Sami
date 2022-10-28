import cv
import datetime
import pandas as pd
#Cerințe suplimentare:

#Se afișează un meniu din care utilizatorul poate alege să realizeze următoarele operații:

#Listare date: în afișarea inițială a datelor se realizează o sortare în funcție de categorie.
#Sortare: se alege o opțiune din cele 8 de mai jos:
#Criteriile disponibile sunt:

#1. sortare ascendentă task

#2. sortare descendentă task

#3. sortare ascendentă data

#4. sortare descendentă data

###   NUMARUL 1  ###
taskuri = pd.read_csv('taskuri.csv', names = ['Task', 'Data', 'Responsabil', 'Categorie'])
taskuri_sortate = taskuri.sort_values(by='Task', ascending=True)
print(taskuri)

###   NUMARUL 2  ###
taskuri = pd.read_csv('taskuri.csv', names = ['Task', 'Data', 'Responsabil', 'Categorie'], index_col='Task')
taskuri_sortate = taskuri.sort_values(ascending=False)

print(taskuri)

#def listare_date():
    #while True:
#        with open('taskuri.csv', 'r') as file:
#            csv_reader = csv.reader(file, deimiter=',')
#            print(list(csv_reader))


#listare_date()