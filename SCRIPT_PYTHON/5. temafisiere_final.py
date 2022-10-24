import csv
import datetime
import pandas as pd


def introducere_categorii():

    while True:
        with open('categorii.txt', 'a') as file:
            file.write(f'{input("Adauga categoria: ")} \n')
            decizie = input("Doriti sa introduceti o alta categorie? (Y/N)").lower()
            if decizie == 'n':
                break
    return True

introducere_categorii()

def validare_data(data_limita):
    try:
        datetime.datetime.strptime(data_limita, '%d-%m-%Y %H:%M')
        return True
    except Exception:
        return False

def introducerea_taskurilor():
    while True:
        with open('taskuri.csv', 'a') as file:
            csv_writer = csv.writer(file, delimiter=',')
            task = input('Adauga un task: ')
            data_limita = input('Adauga o data limita: ')
            validarea_datei = validare_data(data_limita)
            while validarea_datei is False:
                print("Data nu are formatul corect")
                data_limita= input('Adaugati o noua data: ')
                validarea_datei = validare_data(data_limita)
                if validarea_datei is True:
                    break
            responsabil = input('Adauga persoana responsabila: ')
            categoria = input("Adauga categoria: ")
            with open('categorii.txt', 'r') as file:
               line = file.readlines()
            verificare = categoria.strip()
            new_list = [x.strip() for x in line]
            while verificare not in new_list:
                intr_categ = input('Categorie inexistenta. Reintrodu o alta categorie: ')
                if intr_categ:
                    categoria = intr_categ
                if intr_categ.strip() in new_list:
                    break
            csv_writer.writerow([task, data_limita, responsabil, categoria])
        decizie = input("Doriti sa introduceti un alt task? (Y/N)").lower()
        print(decizie)
        if decizie == 'n':
            break

    return True
introducerea_taskurilor()




print("""Metode de sortare: \n
  1. sortare ascendentă task \n
  2. sortare descendentă task \n
  3. sortare ascendentă data task \n
  4. sortare descendentă data \n
  5. sortare ascendentă persoana responsabilă \n
  6. sortare descendentă persoană responsabilă \n
  7. sortare ascendentă categorie \n
  8. sortare descendentă categorie""")
metoda_sortare = input("Alegeti o metoda de sortare: ")

while int(metoda_sortare) not in range(1, 9):
    print("Nu exista metoda")
    input_nou = input("Alege o metoda de sortare de la 1 la 8: ")
    metoda_sortare = input_nou
    if int(input_nou) in range(1, 9):
        break
print(metoda_sortare)


names = ['Task', 'Data', 'Responsabil', 'Categorie']

def sortare(metoda_sortare):
    directie_sortare = True
    if int(metoda_sortare) in range(1,5):
        directie_sortare = True
    elif int(metoda_sortare) in range(5,9):
        directie_sortare = False
        metoda_sortare = int(metoda_sortare) - 5
    df = pd.read_csv('taskuri.csv', names = names, index_col=names[int(metoda_sortare)-1])
    return df.sort_index(ascending= directie_sortare)
print(sortare(metoda_sortare))

print(f"""Coloana filtrare: \n
      1. {names[0]} \n
      2. {names[1]} \n
      3. {names[2]} \n
      4. {names[3]} \n""")

coloana_filtrare = input('Alegeti o coloana de filtrare: ')

while int(coloana_filtrare) not in range(1,5):
    print("Nu exista coloana de filtrare")
    coloana_filtrare_noua = input("Alege o coloana de filtrare de la 1 la 4: ")
    coloana_filtrare = coloana_filtrare_noua
    if int(coloana_filtrare_noua) in range(1,5):
        break
    print(coloana_filtrare)

cheie_filtrare = input('Alegeti o un cuvant pentru a filtra baza de date: ')

def filtrare(coloana_filtrare, cheie_filtrare):
    df = pd.read_csv('taskuri.csv', names=names)
    return df[df[names[int(coloana_filtrare)-1]].str.contains(cheie_filtrare)]
print(filtrare(coloana_filtrare,cheie_filtrare))

df = pd.read_csv('taskuri.csv', names=names)
print(f"\n 'Afisare task-uri existente: '")
print(df)
alegere_adaugare_task = input('Doriti sa adaugati un task?(Y/N)')
# while alegere_adaugare_task.lower() != 'y' or alegere_adaugare_task.lower() != 'n':
#     alegere_adaugare_task = input('Doriti sa adaugati un task?(Y/N)')
#     if alegere_adaugare_task.lower() == 'y' or alegere_adaugare_task.lower() == 'n':
#         break
if alegere_adaugare_task.lower() == 'y':
    print(introducerea_taskurilor())

def editare_task():
    df = pd.read_csv('taskuri.csv', names=names)
    alegere_rand = input("Alegeti un rand pe care sa il editati: ")
    while int(alegere_rand) not in tuple(df.index):
        alegere_rand = input("Alegeti un rand pe care sa il editati: ")
    df.drop([int(alegere_rand)])
    print(introducerea_taskurilor())


alegere_editare_task = input('Doriti sa editati un task?(Y/N)')
# while alegere_editare_task.lower() != 'y' or alegere_editare_task.lower() != 'n':
#     alegere_editare_task = input('Doriti sa editati un task?(Y/N)')
#     if alegere_editare_task.lower() == 'y' or alegere_editare_task.lower() == 'n':
#         break
if alegere_editare_task.lower() == 'y':
    print(editare_task())

def stergere_task():
    df = pd.read_csv('taskuri.csv', names=names)
    alegere_rand = input("Alegeti un rand pe care sa il stergeti: ")
    while int(alegere_rand) not in tuple(df.index):
        alegere_rand = input("Alegeti un rand pe care sa il stergeti: ")
    df.drop([int(alegere_rand)])
    return df

alegere_stergere_task = input('Doriti sa stergeti un task?(Y/N)')
# while alegere_stergere_task.lower() != 'y' or alegere_stergere_task.lower() != 'n':
#     alegere_stergere_task = input('Doriti sa stergeti un task?(Y/N)')
#     if alegere_stergere_task.lower() == 'y' or alegere_stergere_task.lower() == 'n':
#         break
if alegere_stergere_task.lower() == 'y':
    print(stergere_task())