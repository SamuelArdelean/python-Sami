# file = open('data.txt', 'w')
# file.write("hello")
# file.close()

# file = open('data1.txt', 'w')
# try:
#     file.write("hello")
# finally:
#     file.close()

# with open('data2.txt','w') as file:
#     file.write('hello, world!')
#
# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)

# with open('data.txt', 'r') as file:
#     for line in list(file):
#         print(line)

# with open('data.txt', 'r') as file:
#     while True:
#         line=file.readline()
#         if not line:
#             break
#         print(line)

#r -> citim, nu adaugam informatie, este valoarea cu care vine default functia open, daca fisierul nu exista, apare eroare
#w -> scriem, daca fisierul nu exista, il adauga/ sau rescrie daca este in fisier ceva
#a -> scriem, daca exista ceva in fisier, adauga pe deasupra
#r+ -> scriere, citire

# with open('data.txt','r') as file:
#     for line in file.readlines():
#         print('line', line)

# import csv
# with open('data.txt', 'r') as csv_file:
#     rows= csv.reader(csv_file, delimiter =',')
#     for row in rows:
#         print(row)

# new_cars=[['Dacia', 'Logan', 2005, 75],
#           ['Renault', 'Clio', 2005, 75]]
# with open('data.txt', 'a') as csv_file:
#     csv_writer= csv.writer(csv_file, delimiter=',')
#     for new_car in new_cars:
#         csv_writer.writerow(new_car)



import csv
with open('fisiercsv.csv', 'r') as csv_file:
    rows = csv.reader(csv_file, delimiter =',')
    for row in rows:
        print(row)

new_cars = [['Dacia', 'Logan', 2005, 75],
            ['Renault','Clio',2005,75]]

with open('fisiercsv.csv', 'a') as csv_file:
    csv_writer=csv.writer(csv_file, delimiter=',')
    for new_car in new_cars:
        csv_writer.writerow(new_car)


