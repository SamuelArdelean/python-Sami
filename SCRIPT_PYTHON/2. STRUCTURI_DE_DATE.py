'''I. LISTE'''
#LISTE - structuri ordonate(pot fi indexate)/ mutabile/ indexate ( pot fi modificate)
# - fiecare element din lsta are un index
# - numerotarea incepe de la 0 si se termina la n-1 ( n = numarul de elemente din lista)
#my_list = [8, 2, 'a', 8, '4']
# print('mesaj')
# print(my_list[3])
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-5])
# print(len(my_list)) #- lungimea listei
# my_list.append('ana')  - adauga valori la sfarsitul listei
# print(my_list)
# print(my_list.index('a')) - ne arata pozitia nuumarului/ caracterului in lista, doar prima pozitie a indexului gasita

#print(my_list.index(8))
#my_list.insert(4, 'A')
#print(my_list)
#my_list.insert(7,'A') - daca ai la index un nr mai mare decat cat elista de lunga, va pune caracterul la sfarsitul listei

#print(my_list[2:5]) - afiseaza un calup de la o pozitie la cealalta pozitie
#print(my_list[2:1])
#print(my_list[2:3:2])

'''1. METODA SLICE/ IMPARTIRE'''
# - formarea unei noi liste pe baza listei initiale
#my_list = [8, 2, 'a', 8, '4', 5, 10, 'ana', 'masina']
# my_sliced_list = my_list[4:]
# print(my_sliced_list)
#
#my_sliced_list_negativ= my_list[-3:]
#print(my_sliced_list_negativ)
#
# - putem specifica doar indexul de final
# print(my_list[2:4])
# - putem specifica si definirea pasului (din cate in cate elemente sa fie formata noua lista)
#print(my_list[0:7:2])  #- a 3 a cifra reprezinta saltul

'''2. LISTE- FUNCTII'''

# my_list.append() - adauga element nou
#print(my_list.index('ana')) #- returneaza indexul elementului
#my_list.insert(index, element_nou) - adauga un element_nou pe pozitia index
#my_list.insert(3,'A') - daca ai la index un nr mai mare decat cat elista de lunga, va pune caracterul la sfarsitul listei
# my_list.remove(element)_ scoate elementul
# .pop()- scoate utimul element
# .pop(index)- scoate elem de pe pozitia index
# .clear()- scoate toate elementele din lista
# my_list.clear()
# print(my_list)
# .copy()- copiaa lista intr-o alta lista, mai poate fi folosita si functia list(): list(my_list)
# .reverse() - reface lista in ordine inversa
# .sort() - sorteaa ascendent
# .count(element) - returneaza de ate ori se afla elementu in lista
#
# list_3= list_1+list_2  - concatenare a doua liste
# extent(): list_1.extend(list_2)  -  elementele din list_2 vor fi adaugate la finalul listei

'''II. TUPLURI'''
#TUPLURI - seamana cu listele, ordonate, sunt IMUTABILE ( nu pot fi modificabile)
#- TUPLURILE OCUPA MAI PUTINA MEMORIE


#my_tuple = (8, 2, 'a', 8, '4')
#zile_anului = ('luni', )
#zile_anului = tuple()
#zile_anului = ()
#print(type(zile_anului))
#
# lista_1 = ('George', 'Ion', 'Mihai')
# lista_2 = ('Razvan', )
# lista_1 += lista_2
# print(lista_1)

# lista_1 = ('George', 'Ion', 'Mihai')
# (name_1, name_2, name_3) = lista_1
# print(name_1, name_2)
# print(name_2)

'''III. DICTIONARE'''
#DICTIONARE- ORDONATE ( pot fi indexate)/ MUTABILE ( pot fi modificate) - se folosesc {}
#datele sunt reprezntate sub forma de cheie:valoare
# dict_1 = {'key_1': 'valoare',
#          'key_2': 'valoare',
#          3: [1,2,3],
#          4:('valoare_1', 'val_2'),
#          'dict_b':{'dic_c': 3},
#          2+1j: [1,2,5]}
# print(dict_1)
# print(dict_1['key_2'])  #-  printeaza valoarea de pe pozitia respectiva
# print(len(dict_1))  #-  lungimea dictionarului
# print(dict_1.get(3))

# 1. DICTIONARE- FUNCTII
# dict_1.clear() - goleste dictionarul
# .copy() - returneaza o copie
#print(dict_1.keys()) # returneaza un dict_keys continand toate cheile dintr-un ditionar
#.values() - returneaza un dict_values
#print(dict_1.items())  #- retuneaza un dict_items continand toate elementele dintr0un dictionar.
# Un astfel de element reprezinta un tuplu de forma(cheie,valoare)

#.pop(key) - scoade din dictionar cheia key
# print(dict_1.pop(4))
# .popitem() - scoate din dictionar ultimul element introdus

'''SETURI'''
# SETURI - NU SUNT ORDONABILE (nu pot fi indexate)/ NU SUNT MUTABILE - SE FOLOSESC TOT {}
# - ACCESAREA UNUI ELEMENT DIN SET NU ESTE POSIBILA
# set_1 = {'mar', 'para', 'banana', 'mar', 'banana'}
# set_1.remove('para') - da eroare daca nu exista
# set_1.discard('caisa')  - la fel ca remove, sterge elementul
# set_1.pop()  -  scoate din set ultimul element
# set_1.clear()
# print(set_1)
# new_set = set(my_list)
# print(new_set)
# .union() - pentru concatenarea a doua seturi -> returneaza un set nou
# .update() - adauga valorile dintr-un set in altul
# set1 = {1,2,3,4,5}
# set2 = {6,7,8,9}
# set1.update(set2)
# print(set1)

'''TEMA 1
Creați un script Python care îndeplinește următoarele funcții: 
○ declară o listă care conține elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine). 
○ afișează lista inițială ordonată ascendent (lista inițială trebuie păstrată în aceeași formă) 
○ afișează lista inițială ordonată descendent (lista inițială trebuie păstrată în aceeași formă) 
○ afișează o listă ce conține numerele pare din lista ordonată (folosind slice) 
○ afișează o listă ce conține numerele impare din lista ordonată (folosind slice) 
○ afisează o listă ce conține numerele ce sunt multipli ai numărului 3 (folosind slice).'''

# print('lista initiala este formata din: ')
# lista_initiala = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
# print(lista_initiala)
# lista_ascendenta = lista_initiala
# lista_ascendenta.sort()
# print('lista ordonata ascendent = ', lista_ascendenta)
# lista_descendenta = lista_ascendenta
# lista_descendenta.reverse()
# print(' lista ordonata descendent = ', lista_descendenta)
# lista_ascendenta = lista_initiala
# lista_ascendenta.sort()
# print('lista cu valorile pare este = ', lista_ascendenta[1:10:2])
# print('lista cu valorile impare este = ', lista_ascendenta[0:10:2])
# print('lista cu multiplii de 3 este = ', lista_ascendenta[2:10:3])
