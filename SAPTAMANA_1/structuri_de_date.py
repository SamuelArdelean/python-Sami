# structuri de date
#LISTE - structuri ordonate(pot fi indexate)/ mutabile/ indexate ( pot fi modificate)

#my_list = [8, 2, 'a', 8, '4']
#print('mesaj')
#print(my_list[3])
#print(my_list[-1])
#my_list.append('ana')
#print(len(my_list)) - lungimea listei
#my_list.append('ana') - adauga valori la sfarsitul listei
#print(my_list)
#print(my_list.index('a')) - ne arata pozitia nuumarului/ caracterului in lista, doar prima pozitie a indexului gasita

#print(my_list.index(8))
#my_list.insert(4, 'A')
#print(my_list)
#my_list.insert(7,'A') - daca ai la index un nr mai mare decat cat elista de lunga, va pune caracterul la sfarsitul listei

#print(my_list[2:5]) - afiseaza un calup de la o pozitie la cealalta pozitie

#print(my_list[2:1])
#print(my_list[2:3:2])

#my_list.append(['a', 'b', 3,'x',[4,7,'w']])
#print(my_list)
#print(my_list[5])
#print(my_list[6][4][2])
#list_1= [2,3]
#list_2= [2,6]
#list_3= list_1 + list_2
#print(list_3)

#TUPLURI - seamana cu listele, ordonate, sunt IMUTABILE ( nu pot fi modificabile)


#my_tuple = (8, 2, 'a', 8, '4')
#zile_anului = ('luni', )
#zile_anului = tuple()
#zile_anului = ()
#print(type(zile_anului))

#lista_1 = [1]
#lista_1 = ('George', 'Ion', 'Mihai')
#lista_2 = ('Razvan', )
#lista_1 += lista_2
#print(lista_1)

#lista_1 = ('George', 'Ion', 'Mihai')
#(name_1, name_2, name_3) = lista_1
#print(name_1)
#print(name_2)
#choices = [(40, 'Bucuresti'), ]

#lista_1 = ('Ana', 'Ion', 'Mihai', 'Bogdan', 'Ovidiu')
#(name_1, *name_2, name_3) = lista_1
#print(name_1)
#print(name_2)
#print(name_3)

# SETURI - NU SUNT ORDONABILE (nu pot fi indexate)/ NU SUNT MUTABILE

#set_1 = {'mar', 'para', 'banana', 'mar', 'banana'}
#set_1.remove('caisa') - da eroare daca nu exista
#set_1.discard('caisa')
#set_1.pop()
#set_1.clear()
#print(set_1)
#new_set = list(set(my_list)
#print(new_set)

#DICTIONARE- ORDONATE ( pot fi indexate)/ MUTABILE ( pot fi modificate)
#dict_1 = dict()
#dict_2 = {'key_1': 'valoare',
#          'key_2': 'valoare',
#          3: [1,2,3],
#          4:('valoare_1', 'val_2'),
#          'dict_b':{'dic_c': 3},
#          2+1j: [1,2,5]}

#print(dict_2)
#print(len(dict_2))

#print(dict_2.get(5))

#val = dict_2.items()
#dict_2[3] = 'gigel'
#dict_2.update({100:(2, 4)})
#print(dict_2)

#dict_2.popitem()
#print(dict_2)

#CONDITIONARI

#varsta = int(input("va rugam sa introduceti varsta dvs:"))
#if varsta >= 18:
#    print("sunteti eligibil pentru scoala de soferi")
#else:
#    print("sunteti eligibil doar dupa varsta de 18 ani")
#    if varsta == 17:
#        print("mai aveti un an pentru a fi eligibil")

#if varsta>= 65:
#    print("varsta pensionare")
#elif varsta >=15:
#    print("varsta liceu")
#elif varsta >=25:
#    print("varsta facultate")
#else:
#    print("esti micut!")

#WHILE

#print('primul print')
#i = 0
#while i < 3:
#    print('se respecta conditia')
#    print('valoarea este: ' + str(i))
#    i += 1
    #i = i+1
#print(' am ajuns la sfarsit')

#FOR

#list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#for i in list_1:
#    i += 1
#    list_1.append(i)
#print(list_1)
#    print(i)

#my_var = 7
#mesaj = "set instructiuni #3"
#if my_var < 6:
#    mesaj = "set instructiuni #1"
#else:
#    mesaj = "set instructiuni #2"

#print(my_var, mesaj)

#mesaj = "set instructiuni #1" if my_var < 6 else "set instructiuni #2" #operator ternar
#mesaj = "set instructiuni #2"
#if my_var < 6 and (mesaj := "set instructiuni #1"):
#    print(mesaj)

#if 'set' in mesaj:
#    print('exista')
#print(my_var, mesaj)

#a = 1
#b = 2
#impartire = 0
#if a > 0 and b > 0 and (impartire := a / b) and impartire > 1:
 #   print(impartire)
#if a > 0 and b > 0 and a / b > 1:
#    impartire = a / b
#    print(impartire)

#sir = "ana are mere"
#sir1 = list(sir)
#print(sir1)
#for i, v in enumerate(sir): i= index, v= valoare
#    print(i, '=>>', v)
#for variabila_temporara in range(2, len(sir), 3):
#    print(variabila_temporara, '=>>', sir[variabila_temporara])

#dictionar = {'1': 'val1', "2": "val2","3": "val3"}
#print(dictionar["2"])
#print(dictionar)
#dictionar.update({4:"val4"})
#dictionar[5] = 'val5'
#dictionar.update({"3":'val300'})
#for i in dictionar.keys():
#    print(i)
#print(dictionar)

#for i in dictionar:
#    print(i, '->>', dictionar[i])
#print(dictionar)

#LISTE

#my_list = [8, 2, 'a', '4']
#print(my_list[3])
#print(my_list[-1])
#print(len(my_list))
#my_list.append('ANA')   #adauga valori la sfarsit
#print(my_list.index('a')

#print('lista initiala este formata din: ')
#lista_initiala = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
#print(lista_initiala)
#lista_ascendenta = lista_initiala
#lista_ascendenta.sort()
#print('lista ordonata ascendent = ', lista_ascendenta)
#lista_descendenta = lista_initiala
#lista_descendenta.reverse()
#print(' lista ordonata descendent = ', lista_descendenta)
#lista_ascendenta = lista_initiala
#lista_ascendenta.sort()
#print('lista cu valorile pare este = ', lista_ascendenta[1:10:2])
#print('lista cu valorile impare este = ', lista_ascendenta[0:10:2])
#print('lista cu multiplii de 3 este = ', lista_ascendenta[2:10:3])