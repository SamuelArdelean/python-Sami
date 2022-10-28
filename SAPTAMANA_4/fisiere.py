# file = open('data.txt', 'r+')
# file.write("hello ana")
# file.close()



#r -> citim, nu adaugam informatie, este valoarea cu care vine default functia open, daca fisierul nu exista, apare eroare
#w -> scriem, daca fisierul nu exista, il adauga/ sau rescrie daca este in fisier ceva
#a -> scriem, daca exista ceva in fisier, adauga pe deasupra
#r+ -> scriere, citire

# file = open('data1.txt', 'w')
# try:
#     file.write("hello")
# finally:
#     file.close()
#
# with open('data2.txt', 'w') as file:
#     file.write('hello2')

# with open('data.txt', 'r') as file:  #parcurge fiecare linie din fisier si le citeste
#     for line in file.readlines():
#         print(line)

# with open('data.txt', 'r') as file:
#     print(list(file))
#     for line in list(file):
#         print(line)
#
# with open('data.txt', 'r') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)

import csv

# with open('fisiercsv.csv', 'r') as csv_file:   #csv_file este variabila temporara folosita doar in interiorul acestui with
#     rows = csv.reader(csv_file, delimiter=',')  #delimitatorul este virgula
#     for row in rows:
#         print(row)

new_cars = [
    ['Dacia', 'Logan', 2005, 75],
    ['Renault', 'Clio', 2005, 75]
]
with open('fisiercsv.csv','a') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for new_car in new_cars:
        csv_writer.writerow(new_car)
